import importlib, threading
import asyncio, aiocron
import os, pickle, inspect, types, glob, psutil
from functools import wraps, partial
import time, datetime
from collections import OrderedDict

from biothings import config
logger = config.logger

from biothings.utils.hub_db import get_hub_db_conn
from biothings.utils.common import timesofar, get_random_string, sizeof_fmt
from biothings.utils.hub import find_process


def track(func):
    @wraps(func)
    def func_wrapper(*args,**kwargs):
        ptype = args[0] # tracking process or thread ?
        # we're looking for some "pinfo" value (process info) to later
        # reporting. If we can't find any, we'll try our best to figure out
        # what this is about...
        # func is the do_work wrapper, we want the actual partial
        # is first arg a callable (func) or pinfo ?
        if callable(args[1]):
            innerfunc = args[1]
            innerargs = args[2:]
            pinfo = None
        else:
            innerfunc = args[2]
            innerargs = args[3:]
            pinfo = args[1]

        # make sure we can pickle the whole thing (and it's
        # just informative, so stringify is just ok there)
        innerargs = [str(arg) for arg in innerargs]
        if type(innerfunc) == partial:
            fname = innerfunc.func.__name__
        elif type(innerfunc) == types.MethodType:
            fname = innerfunc.__self__.__class__.__name__
        else:
            fname = innerfunc.__name__

        firstarg = innerargs and innerargs[0] or ""
        if not pinfo:
            pinfo = {"category" : None,
                     "source" : None,
                     "step" : None,
                     "description" : "%s %s" % (fname,firstarg)}

        worker = {'func_name' : fname,
                 'args': innerargs, 'kwargs' : kwargs,
                 'started_at': time.time(),
                 'info' : pinfo}
        results = None
        exc = None
        trace = None
        try:
            _id = None
            rnd = get_random_string()
            if ptype == "thread":
                _id = "%s" % threading.current_thread().getName()
            else:
                _id = os.getpid()
            # add random chars: 2 jobs handled by the same slot (pid or thread) 
            # would override filename otherwise
            fn = "%s_%s" % (_id,rnd)
            worker["info"]["id"] = _id
            pidfile = os.path.join(config.RUN_DIR,"%s.pickle" % fn)
            pickle.dump(worker, open(pidfile,"wb"))
            results = func(*args,**kwargs)
        except Exception as e:
            import traceback
            trace = traceback.format_exc()
            logger.error("err %s\n%s" % (e,trace))
            # we want to store exception so for now, just make a reference
            exc = e
        finally:
            if os.path.exists(pidfile):
                pass
                # move to "done" dir and register end of execution time 
                os.rename(pidfile,os.path.join(config.RUN_DIR,"done",os.path.basename(pidfile)))
                pidfile = os.path.join(config.RUN_DIR,"done",os.path.basename(pidfile))
                worker = pickle.load(open(pidfile,"rb"))
                worker["duration"] = timesofar(worker["started_at"])
                worker["err"] = exc
                worker["trace"] = trace
                # try to keep original exception, but this may fail depending on
                # what's in the exception. If we can't, keep the string representation
                try:
                    pickle.dump(worker,open(pidfile,"wb"))
                except Exception:
                    worker["err"] = str(exc)
                    pickle.dump(worker,open(pidfile,"wb"))
        # now raise original exception
        if exc:
            raise exc
        return results
    return func_wrapper

@track
def do_work(ptype, pinfo=None, func=None, *args, **kwargs):
    # pinfo is optional, and func is not. and args and kwargs must 
    # be after func. just to say func is mandatory, despite what the
    # signature says
    assert func
    # need to wrap calls otherwise multiprocessing could have
    # issue pickling directly the passed func because of some import
    # issues ("can't pickle ... object is not the same as ...")
    return func(*args,**kwargs)

class UnknownResource(Exception):
    pass
class ResourceError(Exception):
    pass
class ManagerError(Exception):
    pass
class ResourceNotFound(Exception):
    pass

class BaseManager(object):

    def __init__(self, job_manager):
        self.register = {}
        self.job_manager = job_manager

    def __repr__(self):
        return "<%s [%d registered]: %s>" % (self.__class__.__name__,len(self.register), sorted(list(self.register.keys())))

    def __getitem__(self,src_name):
        try:
            # as a main-source
            return self.register[src_name]
        except KeyError:
            try:
                # as a sub-source
                main,sub = src_name.split(".")
                srcs = self.register[main]
                # there can be many uploader for one resource (when each is dealing
                # with one specific file but upload to the same collection for instance)
                # so we want to make sure user is aware of this and not just return one
                # uploader when many are needed
                # on the other hand, if only one avail, just return it
                res = []
                for src in srcs:
                    if src.name == sub:
                        res.append(src)
                if len(res) == 0:
                    raise KeyError(src_name)
                else:
                    return res
            except (ValueError,AttributeError,KeyError):
                # nope, can't find it...
                raise KeyError(src_name)



class BaseSourceManager(BaseManager):
    """
    Base class to provide source management: discovery, registration
    Actual launch of tasks must be defined in subclasses
    """

    # define the class manager will look for. Set in a subclass
    SOURCE_CLASS = None

    def __init__(self, job_manager, datasource_path="dataload.sources", *args, **kwargs):
        super(BaseSourceManager,self).__init__(job_manager,*args,**kwargs)
        self.conn = get_hub_db_conn()
        self.default_src_path = datasource_path

    def filter_class(self,klass):
        """
        Gives opportunity for subclass to check given class and decide to
        keep it or not in the discovery process. Returning None means "skip it".
        """
        # keep it by default
        return klass

    def register_classes(self,klasses):
        """
        Register each class in self.register dict. Key will be used
        to retrieve the source class, create an instance and run method from it.
        It must be implemented in subclass as each manager may need to access 
        its sources differently,based on different keys.
        """
        raise NotImplementedError("implement me in sub-class")

    def find_classes(self,src_module,fail_on_notfound=True):
        """
        Given a python module, return a list of classes in this module, matching
        SOURCE_CLASS (must inherit from)
        """
        # try to find a uploader class in the module
        found_one = False
        for attr in dir(src_module):
            something = getattr(src_module,attr)
            if type(something) == type and issubclass(something,self.__class__.SOURCE_CLASS):
                klass = something
                if not self.filter_class(klass):
                    continue
                found_one = True
                logger.debug("Found a class based on %s: '%s'" % (self.__class__.SOURCE_CLASS.__name__,klass))
                yield klass
        if not found_one:
            if fail_on_notfound:
                raise UnknownResource("Can't find a class based on %s in module '%s'" % (self.__class__.SOURCE_CLASS.__name__,src_module))
            return []


    def register_source(self, src, fail_on_notfound=True):
        """Register a new data source. src can be a module where some classes
        are defined. It can also be a module path as a string, or just a source name
        in which case it will try to find information from default path.
        """
        if isinstance(src,str):
            try:
                src_m = importlib.import_module(src)
            except ImportError:
                try:
                    src_m = importlib.import_module("%s.%s" % (self.default_src_path,src))
                except ImportError:
                    msg = "Can't find module '%s', even in '%s'" % (src,self.default_src_path)
                    logger.error(msg)
                    raise UnknownResource(msg)

        elif isinstance(src,dict):
            # source is comprised of several other sub sources
            assert len(src) == 1, "Should have only one element in source dict '%s'" % src
            _, sub_srcs = list(src.items())[0]
            for src in sub_srcs:
                self.register_source(src,fail_on_notfound)
            return
        else:
            src_m = src
        klasses = self.find_classes(src_m,fail_on_notfound)
        self.register_classes(klasses)

    def register_sources(self, sources):
        assert not isinstance(sources,str), "sources argument is a string, should pass a list"
        self.register.clear()
        for src in sources:
            try:
                # batch registration, we'll silently ignore not-found sources
                self.register_source(src,fail_on_notfound=False)
            except UnknownResource as e:
                logger.info("Can't register source '%s', skip it; %s" % (src,e))
                import traceback
                logger.error(traceback.format_exc())


class JobManager(object):

    def __init__(self, loop, process_queue=None, thread_queue=None, max_memory_usage=None):
        self.loop = loop
        self.process_queue = process_queue
        self.thread_queue = thread_queue
        self.ok_to_run = asyncio.Semaphore()

        if max_memory_usage == "auto":
            # try to find a nice limit...
            limited = int(psutil.virtual_memory().available * .6)
            logger.info("Auto-setting memory usage limit to %s" % sizeof_fmt(limited))
            max_memory_usage = limited
        elif max_memory_usage:
            logger.info("Setting memory usage to %s" % sizeof_fmt(max_memory_usage))
        self.max_memory_usage = max_memory_usage
        self.avail_memory = int(psutil.virtual_memory().available)
        self._phub = None
        donedir = os.path.join(config.RUN_DIR,"done")
        if not os.path.exists(donedir):
            os.makedirs(donedir)

    @asyncio.coroutine
    def checkmem(self,pinfo=None):
        mem_req = pinfo and pinfo.get("__reqs__",{}).get("mem") or 0
        t0 = time.time()
        waited = False
        sleep_time = 5 
        if mem_req:
            logger.info("Job {cat:%s,source:%s,step:%s} requires %s memory, checking if available" % \
                    (pinfo.get("category"), pinfo.get("source"), pinfo.get("step"), sizeof_fmt(mem_req)))
        if self.max_memory_usage:
            hub_mem = self.hub_memory
            while hub_mem >= self.max_memory_usage:
                logger.info("Hub is using too much memory to launch job {cat:%s,source:%s,step:%s} (%s used, more than max allowed %s), wait a little (job's already been postponed for %s)" % \
                        (pinfo.get("category"), pinfo.get("source"), pinfo.get("step"), sizeof_fmt(hub_mem),
                         sizeof_fmt(self.max_memory_usage),timesofar(t0)))
                yield from asyncio.sleep(sleep_time)
                waited = True
                hub_mem = self.hub_memory
        if mem_req:
            # max allowed mem is either the limit we gave and the os limit
            max_mem = self.max_memory_usage and self.max_memory_usage or self.avail_memory
            # TODO: check projected memory (jobs with mem requirements currently running
            # as those jobs may not have reached their max mem usage yet)
            hub_mem = self.hub_memory
            while mem_req >= (max_mem - hub_mem):
                logger.info("Job {cat:%s,source:%s,step:%s} needs %s to run, not enough to launch it (hub consumes %s while max allowed is %s), wait a little  (job's already been postponed for %s)" % \
                        (pinfo.get("category"), pinfo.get("source"), pinfo.get("step"), sizeof_fmt(mem_req), sizeof_fmt(hub_mem),
                         sizeof_fmt(max_mem), timesofar(t0)))
                yield from asyncio.sleep(sleep_time)
                waited = True
                # refresh limites and usage (manager can be modified from hub
                # thus memory usage can be modified on-the-fly
                hub_mem = self.hub_memory
                max_mem = self.max_memory_usage and self.max_memory_usage or self.avail_memory
        pendings = len(self.process_queue._pending_work_items.keys()) - config.HUB_MAX_WORKERS
        while pendings >= config.MAX_QUEUED_JOBS:
            if not waited:
                logger.info("Can't run job {cat:%s,source:%s,step:%s} right now, too much pending jobs in the queue (max: %s), will retry until possible" % \
                        (pinfo.get("category"), pinfo.get("source"), pinfo.get("step"), config.MAX_QUEUED_JOBS))
            yield from asyncio.sleep(sleep_time)
            pendings = len(self.process_queue._pending_work_items.keys()) - config.HUB_MAX_WORKERS
            waited = True
        if waited:
            logger.info("Job {cat:%s,source:%s,step:%s} now can be launched (total waiting time: %s)" % (pinfo.get("category"),
                pinfo.get("source"), pinfo.get("step"), timesofar(t0)))

    @asyncio.coroutine
    def defer_to_process(self, pinfo=None, func=None, *args):

        @asyncio.coroutine
        def run(future):
            yield from self.checkmem(pinfo)
            self.ok_to_run.release()
            res = yield from self.loop.run_in_executor(self.process_queue,
                    partial(do_work,"process",pinfo,func,*args))
            # process could generate other parallelized jobs and return a Future/Task
            # If so, we want to make sure we get the results from that task
            if type(res) == asyncio.Task:
                res = yield from res
            future.set_result(res)
        yield from self.ok_to_run.acquire()
        f = asyncio.Future()
        def runned(innerf):
            if innerf.exception():
                f.set_exception(innerf.exception())
        fut = asyncio.ensure_future(run(f))
        fut.add_done_callback(runned)
        return f

    @asyncio.coroutine
    def defer_to_thread(self, pinfo=None, func=None, *args):

        @asyncio.coroutine
        def run(future):
            yield from self.checkmem(pinfo)
            self.ok_to_run.release()
            res = yield from self.loop.run_in_executor(self.thread_queue,
                    partial(do_work,"thread",pinfo,func,*args))
            # thread could generate other parallelized jobs and return a Future/Task
            # If so, we want to make sure we get the results from that task
            if type(res) == asyncio.Task:
                res = yield from res
            future.set_result(res)
        yield from self.ok_to_run.acquire()
        f = asyncio.Future()
        def runned(innerf):
            if innerf.exception():
                f.set_exception(innerf.exception())
        fut = asyncio.ensure_future(run(f))
        fut.add_done_callback(runned)
        return f

    def submit(self,pfunc,schedule=None):
        """
        Helper to submit and run tasks. Tasks will run async'ly.
        pfunc is a functools.partial
        schedule is a string representing a cron schedule, task will then be scheduled
        accordingly.
        """
        logger.info("Building task: %s" % pfunc)
        if schedule:
            logger.info("Scheduling task %s: %s" % (pfunc,schedule))
            cron = aiocron.crontab(schedule,func=pfunc, start=True, loop=self.loop)
            return cron
        else:
            ff = asyncio.ensure_future(pfunc())
            return ff

    @property
    def hub_process(self):
        if not self._phub:
            self._phub = find_process(os.getpid())
        return self._phub

    @property
    def hub_memory(self):
        procs = [self.hub_process] + self.hub_process.children()
        total_mem = 0
        for proc in procs:
            total_mem += proc.memory_info().rss
        return total_mem

    def get_pid_files(self, child=None):
        pat = re.compile(".*/(\d+)_.*\.pickle") # see track() for filename format
        pchildren = self.hub_process.phub.children()
        children_pids = [p.pid for p in pchildren]
        pids = {}
        for fn in glob.glob(os.path.join(config.RUN_DIR,"*.pickle")):
            try:
                pid = int(pat.findall(fn)[0].split("_")[0])
                if not pid in children_pids:
                    print("Removing staled pid file '%s'" % fn)
                    os.unlink(fn)
                else:
                    if not child or child.pid == pid:
                        worker = pickle.load(open(fn,"rb"))
                        worker["process"] = pchildren[children_pids.index(pid)]
                        pids[pid] = worker
            except IndexError:
                # weird though... should have only pid files there...
                pass
        return pids

    def get_thread_files(self):
        # see track() for filename format
        pat = re.compile(".*/(Thread-\d+)_.*\.pickle")
        threads = self.thread_queue._threads
        active_tids = [t.getName() for t in threads]
        tids = {}
        for fn in glob.glob(os.path.join(config.RUN_DIR,"*.pickle")):
            try:
                tid = pat.findall(fn)[0].split("_")[0]
                if not tid in active_tids:
                    print("Removing staled thread file '%s'" % fn)
                    os.unlink(fn)
                else:
                    worker = pickle.load(open(fn,"rb"))
                    worker["process"] = self.hub_process # misleading... it's the hub process
                    tids[tid] = worker
            except IndexError:
                # weird though... should have only pid files there...
                pass
        return tids

    def extract_pending_info(self, pending):
        info = pending.fn.args[1]
        assert type(info) == dict
        return info

    def extract_worker_info(self, worker):
        info = OrderedDict()
        proc = worker.get("process")
        err = worker.get("err") and " !" or ""
        info["pid"] = str(worker["info"]["id"]) + err
        info["source"] = norm(worker["info"].get("source") or "",25)
        info["category"] = norm(worker["info"].get("category") or "",10)
        info["step"] = norm(worker["info"].get("step") or "",20)
        info["description"] = norm(worker["info"].get("description") or "",30)
        info["mem"] = proc and sizeof_fmt(proc.memory_info().rss)
        info["cpu"] = proc and "%.1f%%" % proc.cpu_percent()
        info["started_at"] = worker.get("started_at") or ""
        if worker.get("duration"):
            info["duration"] = worker["duration"]
        else:
            info["duration"] = timesofar(worker.get("started_at",0))
        info["files"] = []
        if proc:
            for pfile in proc.open_files():
                # skip 'a' (logger)
                if pfile.mode == 'r':
                    finfo = OrderedDict()
                    finfo["path"] = pfile.path
                    finfo["read"] = sizeof_fmt(pfile.position)
                    size = os.path.getsize(pfile.path)
                    finfo["size"] = sizeof_fmt(size)
                    info["files"].append(finfo)
        return info

    def get_pendings(self, running=None):
        # pendings are kept in queue while running, until result is there so we need
        # to adjust the actual real pending jobs. also, pending job are get() from the
        # queue following FIFO order. finally, worker ID is incremental. So...
        pendings = sorted(self.process_queue._pending_work_items.items())
        if not running:
            running = len(self.get_pid_files())
        actual_pendings = pendings[running:]
        for pending in actual_pendings:
            yield self.extract_pending_info(pending)

    def get_dones(self, jobs=None, purge=True):
        if jobs is None:
            jobs = glob.glob(os.path.join(config.RUN_DIR,"done","*.pickle"))
        if jobs:
            jfiles_workers = [(jfile,pickle.load(open(jfile,"rb"))) for jfile in jobs]
            # sort by start time
            jfiles_workers = sorted(jfiles_workers,key=lambda e: e[1]["started_at"])
            for jfile,worker in jfiles_workers:
                info = extract_worker_info(worker)
                # format start time
                tt = datetime.datetime.fromtimestamp(info["started_at"]).timetuple()
                info["started_at"] = time.strftime("%Y/%m/%d %H:%M:%S",tt)
                yield info
                if purge:
                    os.unlink(jfile)

    def get_runs(self, pworkers=None, tworkers=None):
        for workers in [pworkers,tworkers]:
            if workers:
                for pid in workers:
                    worker = workers[pid]
                    info = extract_worker_info(worker)
                    tt = datetime.datetime.fromtimestamp(info["started_at"]).timetuple()
                    info["started_at"] = time.strftime("%Y/%m/%d %H:%M:%S",tt)
                    yield info

    def top(self, action="summary"):
        pending = False
        done = False
        run = False
        pid = None
        child = None
        if action:
            try:
                # want to see details for a specific process ?
                pid = int(action)
                child = [p for p in pchildren if p.pid == pid][0]
            except ValueError:
                pass
        pworkers = get_pid_files(pchildren,child)
        tworkers = get_thread_files(phub, threads)
        done_jobs = glob.glob(os.path.join(config.RUN_DIR,"done","*.pickle"))
        if child:
            return pworkers[child.pid]
        elif action == "pending":
            return self.get_pendings(running=len(pworkers))
        elif action == "done":
            return self.get_dones(done_jobs)
        elif action == "run":
            return self.get_runs(pworkers,tworkers)
        elif action == "summary":
            return self.get_summary()
        else:
            raise ValueError("Unknown action '%s'" % action)

