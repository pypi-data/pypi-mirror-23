import sys, re, math
import os, glob
import time
import copy
import importlib
import pickle
from datetime import datetime
from pprint import pformat
import asyncio
from functools import partial
import glob, random
import aiocron

from biothings.utils.common import timesofar, iter_n, get_timestamp, \
                                   dump, rmdashfr, loadobj
from biothings.utils.mongo import doc_feeder, id_feeder
from biothings.utils.loggers import get_logger, HipchatHandler
from biothings.databuild.mapper import TransparentMapper
from biothings.dataload.uploader import ResourceNotReady
from biothings.utils.manager import BaseManager, ManagerError
from biothings.utils.dataload import update_dict_recur
import biothings.utils.mongo as mongo
from biothings.utils.hub_db import get_source_fullname, get_src_build_config, \
                                   get_src_build, get_src_dump, get_src_master
import biothings.databuild.backend as backend
from biothings.databuild.backend import TargetDocMongoBackend
from biothings import config as btconfig

logging = btconfig.logger

class BuilderException(Exception):
    pass
class ResumeException(Exception):
    pass


class DataBuilder(object):

    keep_archive = 10 # number of archived collection to keep. Oldest get dropped first.

    def __init__(self, build_name, source_backend, target_backend, log_folder,
                 doc_root_key="root", mappers=[], default_mapper_class=TransparentMapper,
                 sources=None, target_name=None,**kwargs):
        self.init_state()
        self.build_name = build_name
        self.sources = sources
        self.target_name = target_name
        if type(source_backend) == partial:
            self._partial_source_backend = source_backend
        else:
            self._state["source_backend"] = source_backend
        if type(target_backend) == partial:
            self._partial_target_backend = target_backend
        else:
            self._state["target_backend"] = target_backend
        # doc_root_key is a key name within src_build_config doc.
        # it's a list of datasources that are able to create a document
        # even it doesn't exist. It root documents list is not empty, then
        # any other datasources not listed there won't be able to create
        # a document, only will they able to update it.
        # If no root documets, any datasources can create/update a doc
        # and thus there's no priority nor limitations
        # note: negations can be used, like "!source1". meaning source1 is not
        # root document datasource.
        # Usefull to express; "all resources except source1"
        self.doc_root_key = doc_root_key
        self.t0 = time.time()
        self.logfile = None
        self.log_folder = log_folder
        self.mappers = {}
        self.timestamp = datetime.now()
        self.stats = {} # keep track of cnt per source, etc...
        self.src_versions = {} # versions involved in this build
        self.metadata = {} # custom metadata
        self.mapping = {} # ES mapping (merged from src_master's docs)

        for mapper in mappers + [default_mapper_class()]:
            self.mappers[mapper.name] = mapper

        self.step = kwargs.get("step",10000)
        self.prepared = False

    def init_state(self):
        self._state = {
                "logger" : None,
                "source_backend" : None,
                "target_backend" : None,
                "build_config" : None,
        }
    @property
    def logger(self):
        if not self._state["logger"]:
            self.prepare()
        return self._state["logger"]
    @property
    def source_backend(self):
        if self._state["source_backend"] is None:
            self.prepare()
            self._state["build_config"] = self._state["source_backend"].get_build_configuration(self.build_name)
            self._state["source_backend"].validate_sources(self.sources)
        return self._state["source_backend"]
    @property
    def target_backend(self):
        if self._state["target_backend"] is None:
            self.prepare()
        return self._state["target_backend"]
    @property
    def build_config(self):
        self._state["build_config"] = self.source_backend.get_build_configuration(self.build_name)
        return self._state["build_config"]
    @logger.setter
    def logger(self, value):
        self._state["logger"] = value
    @build_config.setter
    def build_config(self, value):
        self._state["build_config"] = value

    def prepare(self,state={}):
        if self.prepared:
            return
        if state:
            # let's be explicit, _state takes what it wants
            for k in self._state:
                self._state[k] = state[k]
            return
        self._state["source_backend"] = self._partial_source_backend()
        self._state["target_backend"] = self._partial_target_backend()
        self.setup()
        self.setup_log()
        self.prepared = True

    def unprepare(self):
        """
        reset anything that's not pickable (so self can be pickled)
        return what's been reset as a dict, so self can be restored
        once pickled
        """
        # TODO: use copy ?
        state = {
            "logger" : self._state["logger"],
            "source_backend" : self._state["source_backend"],
            "target_backend" : self._state["target_backend"],
            "build_config" : self._state["build_config"],
        }
        for k in state:
            self._state[k] = None
        self.prepared = False
        return state

    def get_pinfo(self):
        """
        Return dict containing information about the current process
        (used to report in the hub)
        """
        return {"category" : "builder",
                "source" : "%s:%s" % (self.build_name,self.target_backend.target_name),
                "step" : "",
                "description" : ""}

    def setup_log(self):
        # TODO: use bt.utils.loggers.get_logger
        import logging as logging_mod
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)
        self.logfile = os.path.join(self.log_folder, 'build_%s_%s.log' % (self.build_name,time.strftime("%Y%m%d",self.timestamp.timetuple())))
        fh = logging_mod.FileHandler(self.logfile)
        fmt = logging_mod.Formatter('%(asctime)s [%(process)d:%(threadName)s] - %(name)s - %(levelname)s -- %(message)s',datefmt="%H:%M:%S")
        fh.setFormatter(fmt)
        fh.name = "logfile"
        nh = HipchatHandler(btconfig.HIPCHAT_CONFIG)
        nh.setFormatter(fmt)
        nh.name = "hipchat"
        self.logger = logging_mod.getLogger("%s_build" % self.build_name)
        self.logger.setLevel(logging_mod.DEBUG)
        if not fh.name in [h.name for h in self.logger.handlers]:
            self.logger.addHandler(fh)
        if not nh.name in [h.name for h in self.logger.handlers]:
            self.logger.addHandler(nh)
        return self.logger

    def check_ready(self,force=False):
        if force:
            # don't even bother
            return
        src_build_config = self.source_backend.build_config
        src_dump = self.source_backend.dump
        _cfg = src_build_config.find_one({'_id': self.build_config['_id']})
        # check if all resources are uploaded
        for src_name in _cfg["sources"]:
            fullname = get_source_fullname(src_name)
            if not fullname:
                raise ResourceNotReady("Can't find source '%s'" % src_name)
            main_name = fullname.split(".")[0]
            src_doc = src_dump.find_one({"_id":main_name})
            if not src_doc:
                raise ResourceNotReady("Missing information for source '%s' to start merging" % src_name)
            if not src_doc.get("upload",{}).get("jobs",{}).get(src_name,{}).get("status") == "success":
                raise ResourceNotReady("No successful upload found for resource '%s'" % src_name)

    def get_build_version(self):
        """
        Generate an arbitrary major build version. Default is using a timestamp (YYMMDD)
        '.' char isn't allowed in build version as it's reserved for minor versions
        """
        d = datetime.fromtimestamp(self.t0)
        return "%d%02d%02d" % (d.year,d.month,d.day)

    def register_status(self,status,transient=False,init=False,**extra):
        """
        Register current build status. A build status is a record in src_build
        The key used in this dict the target_name. Then, any operation
        acting on this target_name is registered in a "jobs" list.
        """
        assert self.build_config, "build_config needs to be specified first"
        # get it from source_backend, kind of weird...
        src_build = self.source_backend.build
        src_build_config = self.source_backend.build_config
        all_sources = self.build_config.get("sources",[])
        target_name = "%s" % self.target_backend.target_name
        build_info = {
                '_id' : target_name,
                'target_backend': self.target_backend.name,
                'target_name': target_name,
                'build_config': self.build_config,
                # these are all the sources required to build target
                # (not just the ones being processed, those are registered in jobs
                'sources' : all_sources, 
                }
        job_info = {
                'status': status,
                'step_started_at': datetime.now(),
                'logfile': self.logfile,
                }
        if status == "building":
            # reset the flag
            src_build_config.update({"_id" : self.build_config["_id"]},{"$unset" : {"pending_to_build":None}})
        if transient:
            # record some "in-progress" information
            job_info['pid'] = os.getpid()
        else:
            # only register time when it's a final state
            job_info["time"] = timesofar(self.t0)
            t1 = round(time.time() - self.t0, 0)
            job_info["time_in_s"] = t1
        if "build" in extra:
            build_info.update(extra["build"])
        if "job" in extra:
            job_info.update(extra["job"])
        # create a new build entry in "build" dict if none exists
        build = src_build.find_one({'_id': target_name})
        if not build:
            # first record for target_name, keep a timestamp
            build_info["started_at"] = datetime.fromtimestamp(self.t0)
            build_info["jobs"] = []
            src_build.insert_one(build_info)
        if init:
            src_build.update({'_id': target_name}, {"$push": {'jobs': job_info}})
            # now refresh/sync
            build = src_build.find_one({'_id': target_name})
        else:
            # merge extra at root level
            # (to keep building data...) and update the last one
            # (it's been properly created before when init=True)
            build["jobs"][-1].update(job_info)
            # build_info is common to all jobs, so we want to keep
            # any existing data (well... except if it's explicitely specified)
            def merge_build_info(target,d):
                if "__REPLACE__" in d.keys():
                    d.pop("__REPLACE__")
                    target = d
                else:
                    for k,v in d.items():
                        if type(v) == dict:
                            if k in target:
                                target[k] = merge_build_info(target[k],v) 
                            else:
                                v.pop("__REPLACE__",None)
                                # merge v with "nothing" just to make sure to remove any "__REPLACE__"
                                v = merge_build_info({},v)
                                target[k] = v
                        else:
                            target[k] = v
                return target
            build = merge_build_info(build,build_info)
            src_build.replace_one({"_id" : build["_id"]}, build)

    def clean_old_collections(self):
        # use target_name is given, otherwise build name will be used 
        # as collection name prefix, so they should start like that
        prefix = "%s_" % (self.target_name or self.build_name)
        db = mongo.get_target_db()
        cols = [c for c in db.collection_names() if c.startswith(prefix)]
        # timestamp is what's after _archive_, YYYYMMDD, so we can sort it safely
        cols = sorted(cols,reverse=True)
        to_drop = cols[self.keep_archive:]
        for colname in to_drop:
            self.logger.info("Cleaning old archive collection '%s'" % colname)
            db[colname].drop()

    def init_mapper(self,mapper_name):
        if self.mappers[mapper_name].need_load():
            if mapper_name is None:
                self.logger.info("Initializing default mapper")
            else:
                self.logger.info("Initializing mapper name '%s'" % mapper_name)
            self.mappers[mapper_name].load()

    def generate_document_query(self, src_name):
        return None

    def get_root_document_sources(self):
        root_srcs = self.build_config.get(self.doc_root_key,[]) or []
        # check for "not this resource" and adjust the list
        none_root_srcs = [src.replace("!","") for src in root_srcs if src.startswith("!")]
        if none_root_srcs:
            if len(none_root_srcs) != len(root_srcs):
                raise BuilderException("If using '!' operator, all datasources must use it (cannot mix), got: %s" % \
                        (repr(root_srcs)))
            # ok, grab sources for this build, 
            srcs = self.build_config.get("sources",[])
            root_srcs = list(set(srcs).difference(set(none_root_srcs)))
            #self.logger.info("'except root' sources %s resolves to root source = %s" % (repr(none_root_srcs),root_srcs))

        # resolve possible regex based source name (split-collections sources)
        root_srcs = self.resolve_sources(root_srcs)
        return root_srcs

    def setup(self,sources=None, target_name=None):
        sources = sources or self.sources
        target_name = target_name or self.target_name
        self.target_backend.set_target_name(self.target_name, self.build_name)
        # root key is optional but if set, it must exist in build config
        if self.doc_root_key and not self.doc_root_key in self.build_config:
            raise BuilderException("Root document key '%s' can't be found in build configuration" % self.doc_root_key)

    def get_metadata(self,sources,job_manager):
        """
        Return a dictionnary of metadata for this build. It's usually app-specific 
        and this method may be overridden as needed. Default: return "merge_stats"
        (#docs involved in each single collections used in that build)

        Return dictionary will potentially be merged with existing metadata in
        src_build collection. This behavior can be changed by setting a special
        key within metadata dict: {"__REPLACE__" : True} will... replace existing 
        metadata with the one returned here.

        "job_manager" is passed in case parallelization is needed. Be aware
        that this method is already running in a dedicated thread, in order to
        use job_manager, the following code must be used at the very beginning 
        of its implementation:
        asyncio.set_event_loop(job_manager.loop)
        """
        return self.stats

    def get_mapping(self,sources):
        """
        Merge mappings from src_master
        """
        mapping = {}
        src_master = self.source_backend.master
        for collection in self.build_config['sources']:
            meta = src_master.find_one({"_id" : collection})
            if 'mapping' in meta and meta["mapping"]:
                mapping.update(meta['mapping'])
            else:
                self.logger.info('Warning: "%s" collection has no mapping data.' % collection)
        return mapping

    def store_metadata(self,res,sources,job_manager):
        self.target_backend.post_merge()
        self.src_meta = self.source_backend.get_src_metadata()
        # TODO: backward compatible src_version key, should be removed
        # eventually as all informations are avail in src_meta
        self.src_versions = self.src_meta.pop("src_version")
        self.mapping = self.get_mapping(sources)
        self.metadata = self.get_metadata(sources,job_manager)

    def resolve_sources(self,sources):
        """
        Source can be a string that may contain regex chars. It's usefull
        when you have plenty of sub-collections prefixed with a source name.
        For instance, given a source named 'blah' stored in as many collections
        as chromosomes, insteand of passing each name as 'blah_1', 'blah_2', etc...
        'blah_.*' can be specified in build_config. This method resolves potential
        regexed source name into real, existing collection names
        """
        if type(sources) == str:
            sources = [sources]
        src_db = mongo.get_src_db()
        cols = src_db.collection_names()
        masters = self.source_backend.get_src_master_docs()
        found = []
        for src in sources:
            # check if master _id and name are different (meaning name is a regex)
            master = masters.get(src)
            if not master:
                raise BuilderException("'%s'could not be found in master documents (%s)" % \
                        (src,repr(list(masters.keys()))))
            search = src
            if master["_id"] != master["name"]:
                search = master["name"]
            # restrict pattern to minimal match
            pat = re.compile("^%s$" % search)
            for col in cols:
                if pat.match(col):
                    found.append(col)
        return found

    def merge(self, sources=None, target_name=None, force=False, ids=None,steps=["merge","post","metadata"],
            job_manager=None, *args,**kwargs):
        assert job_manager
        # check what to do
        if type(steps) == str:
            steps = [steps]
        self.t0 = time.time()
        self.check_ready(force)
        # normalize
        avail_sources = self.build_config['sources']
        if sources is None:
            self.target_backend.drop()
            self.target_backend.prepare()
            sources = avail_sources # merge all
        elif isinstance(sources,str):
            sources = [sources]

        orig_sources = sources
        sources = self.resolve_sources(sources)
        if not sources:
            raise BuilderException("No source found, got %s while available sources are: %s" % \
                    (repr(orig_sources),repr(avail_sources)))
        if target_name:
            self.target_name = target_name
            self.target_backend.set_target_name(self.target_name)
        else:
            target_name = self.target_backend.target_collection.name
        self.clean_old_collections()

        self.logger.info("Merging into target collection '%s'" % self.target_backend.target_collection.name)
        strargs = "[sources=%s,target_name=%s]" % (sources,target_name)

        try:
            @asyncio.coroutine
            def do():
                res = None
                if "merge" in steps:
                    job = self.merge_sources(source_names=sources, ids=ids, steps=steps,
                            job_manager=job_manager, *args, **kwargs)
                    res = yield from job
                if "metadata" in steps:
                    pinfo = self.get_pinfo()
                    pinfo["step"] = "metadata"
                    postjob = yield from job_manager.defer_to_thread(pinfo,
                            partial(self.store_metadata,res,sources=sources,job_manager=job_manager))
                    def stored(f):
                        try:
                            nonlocal res
                            if res:
                                res = f.result() # consume to trigger exceptions if any
                            strargs = "[sources=%s,stats=%s,versions=%s]" % \
                                    (sources,self.stats,self.src_versions)
                            build_version = self.get_build_version()
                            if "." in build_version:
                                raise BuilderException("Can't use '.' in build version '%s', it's reserved for minor versions" % build_version)
                            # get original start dt
                            src_build = self.source_backend.build
                            build = src_build.find_one({'_id': target_name})
                            self.register_status('success',build={
                                "merge_stats" : self.stats,
                                "mapping" : self.mapping,
                                "_meta" : {
                                    "src_version" : self.src_versions,
                                    "src" : self.src_meta,
                                    "stats" : self.metadata,
                                    "build_version" : build_version,
                                    "timestamp" : build["started_at"].isoformat()}
                                })
                            self.logger.info("success %s" % strargs,extra={"notify":True})
                        except Exception as e:
                            strargs = "[sources=%s]" % sources
                            self.register_status("failed",job={"err": repr(e)})
                            self.logger.exception("failed %s: %s" % (strargs,e),extra={"notify":True})
                            raise
                    postjob.add_done_callback(stored)
                    yield from postjob

            task = asyncio.ensure_future(do())
            return task

        except (KeyboardInterrupt,Exception) as e:
            self.logger.exception(e)
            self.register_status("failed",job={"err": repr(e)})
            self.logger.exception("failed %s: %s" % (strargs,e),extra={"notify":True})
            raise

    def get_mapper_for_source(self,src_name,init=True):
        # src_name can be a regex (when source has split collections, they are merge but
        # comes from the same "template" sourcek
        docs = self.source_backend.get_src_master_docs()
        mapper_name = None
        for master_name in docs:
            pat = re.compile("^%s$" % master_name)
            if pat.match(src_name):
                mapper_name = docs[master_name].get("mapper")
        # TODO: this could be a list
        try:
            init and self.init_mapper(mapper_name)
            mapper = self.mappers[mapper_name]
            self.logger.info("Found mapper '%s' for source '%s'" % (mapper,src_name))
            return mapper
        except KeyError:
            raise BuilderException("Found mapper named '%s' but no mapper associated" % mapper_name)

    @asyncio.coroutine
    def merge_sources(self, source_names, steps=["merge","post"], batch_size=100000, ids=None, job_manager=None):
        """
        Merge resources from given source_names or from build config.
        Identify root document sources from the list to first process them.
        ids can a be list of documents to be merged in particular.
        """
        assert job_manager
        # check what to do
        if type(steps) == str:
            steps = [steps]
        do_merge = "merge" in steps
        do_post_merge = "post" in steps
        total_docs = 0
        self.stats = {}
        self.src_versions = {}
        self.metadata = {}
        self.mapping = {}
        # try to identify root document sources amongst the list to first
        # process them (if any)
        defined_root_sources = self.get_root_document_sources()
        root_sources = list(set(source_names).intersection(set(defined_root_sources)))
        other_sources = list(set(source_names).difference(set(root_sources)))
        # got root doc sources but not part of the merge ? that's weird...
        if defined_root_sources and not root_sources:
            self.logger.warning("Root document sources found (%s) but not part of the merge..." % defined_root_sources)

        source_names = sorted(source_names)
        root_sources = sorted(root_sources)
        other_sources = sorted(other_sources)

        self.logger.info("Sources to be merged: %s" % source_names)
        self.logger.info("Root sources: %s" % root_sources)
        self.logger.info("Other sources: %s" % other_sources)

        got_error = False

        @asyncio.coroutine
        def merge(src_names):
            jobs = []
            for i,src_name in enumerate(src_names):
                yield from asyncio.sleep(0.0)
                job = self.merge_source(src_name, batch_size=batch_size, ids=ids,
                                        job_manager=job_manager)
                job = asyncio.ensure_future(job)
                def merged(f,name,stats):
                    try:
                        res = f.result()
                        stats.update(res)
                    except Exception as e:
                        self.logger.exception("Failed merging source '%s': %s" % (name, e))
                        nonlocal got_error
                        got_error = e
                job.add_done_callback(partial(merged,name=src_name,stats=self.stats))
                jobs.append(job)
                yield from asyncio.wait([job])
                # raise error as soon as we know something went wrong
                if got_error:
                    raise got_error
            tasks = asyncio.gather(*jobs)
            yield from tasks

        if do_merge:
            if root_sources:
                self.register_status("building",transient=True,init=True,
                        job={"step":"merge-root","sources":root_sources})
                self.logger.info("Merging root document sources: %s" % root_sources)
                yield from merge(root_sources)
                self.register_status("success",job={"step":"merge-root","sources":root_sources})

            if other_sources:
                self.register_status("building",transient=True,init=True,
                        job={"step":"merge-others","sources":other_sources})
                self.logger.info("Merging other resources: %s" % other_sources)
                yield from merge(other_sources)
                self.register_status("success",job={"step":"merge-others","sources":other_sources})

            self.register_status("building",transient=True,init=True,
                    job={"step":"finalizing"})
            self.logger.info("Finalizing target backend")
            self.target_backend.finalize()
            self.register_status("success",job={"step":"finalizing"})
        else:
            self.logger.info("Skip data merging")

        if do_post_merge:
            self.logger.info("Running post-merge process")
            self.register_status("building",transient=True,init=True,job={"step":"post-merge"})
            pinfo = self.get_pinfo()
            pinfo["step"] = "post-merge"
            job = yield from job_manager.defer_to_thread(pinfo,partial(self.post_merge, source_names, batch_size, job_manager))
            job = asyncio.ensure_future(job)
            def postmerged(f):
                try:
                    self.logger.info("Post-merge completed [%s]" % f.result())
                    self.register_status("success",job={"step":"post-merge"})
                except Exception as e:
                    self.logger.exception("Failed post-merging source: %s" % e)
                    nonlocal got_error
                    got_error = e
            job.add_done_callback(postmerged)
            res = yield from job
            if got_error:
                raise got_error
        else:
            self.logger.info("Skip post-merge process")

        yield from asyncio.sleep(0.0)
        return self.stats

    def clean_document_to_merge(self,doc):
        return doc

    @asyncio.coroutine
    def merge_source(self, src_name, batch_size=100000, ids=None, job_manager=None):
        # it's actually not optional
        assert job_manager
        _query = self.generate_document_query(src_name)
        # Note: no need to check if there's an existing document with _id (we want to merge only with an existing document)
        # if the document doesn't exist then the update() call will silently fail.
        # That being said... if no root documents, then there won't be any previously inserted
        # documents, and this update() would just do nothing. So if no root docs, then upsert
        # (update or insert, but do something)
        defined_root_sources = self.get_root_document_sources()
        upsert = not defined_root_sources or src_name in defined_root_sources
        if not upsert:
            self.logger.debug("Documents from source '%s' will be stored only if a previous document exists with same _id" % src_name)
        jobs = []
        total = self.source_backend[src_name].count()
        btotal = math.ceil(total/batch_size) 
        bnum = 1
        cnt = 0
        got_error = False
        # grab ids only, so we can get more, let's say 10 times more
        id_batch_size = batch_size * 10
        if ids:
            self.logger.info("Merging '%s' specific list of _ids, create merger job with batch_size=%d" % (src_name, batch_size))
            id_provider = [ids]
        else:
            self.logger.info("Fetch _ids from '%s' with batch_size=%d, and create merger job with batch_size=%d" % (src_name, id_batch_size, batch_size))
            id_provider = id_feeder(self.source_backend[src_name], batch_size=id_batch_size)
        id_provider = ids and [ids] or id_feeder(self.source_backend[src_name],
                                                 batch_size=id_batch_size,logger=self.logger)
        for big_doc_ids in id_provider:
            for doc_ids in iter_n(big_doc_ids,batch_size):
                # try to put some async here to give control back
                # (but everybody knows it's a blocking call: doc_feeder)
                yield from asyncio.sleep(0.1)
                cnt += len(doc_ids)
                pinfo = self.get_pinfo()
                pinfo["step"] = src_name
                pinfo["description"] = "#%d/%d (%.1f%%)" % (bnum,btotal,(cnt/total*100))
                self.logger.info("Creating merger job #%d/%d, to process '%s' %d/%d (%.1f%%)" % \
                        (bnum,btotal,src_name,cnt,total,(cnt/total*100.)))
                job = yield from job_manager.defer_to_process(
                        pinfo,
                        partial(merger_worker,
                            self.source_backend[src_name].name,
                            self.target_backend.target_name,
                            doc_ids,
                            self.get_mapper_for_source(src_name,init=False),
                            upsert,
                            bnum))
                def batch_merged(f,batch_num):
                    nonlocal got_error
                    if type(f.result()) != int:
                        got_error = Exception("Batch #%s failed while merging source '%s' [%s]" % (batch_num,src_name,f.result()))
                job.add_done_callback(partial(batch_merged,batch_num=bnum))
                jobs.append(job)
                bnum += 1
                # raise error as soon as we know
                if got_error:
                    raise got_error
        self.logger.info("%d jobs created for merging step" % len(jobs))
        tasks = asyncio.gather(*jobs)
        def done(f):
            nonlocal got_error
            if None in f.result():
                got_error = Exception("Some batches failed")
                return
            # compute overall inserted/updated records
            cnt = sum(f.result())

        tasks.add_done_callback(done)
        yield from tasks
        if got_error:
            raise got_error
        else:
            return {"%s" % src_name : cnt}

    def post_merge(self, source_names, batch_size, job_manager):
        pass


from biothings.utils.backend import DocMongoBackend

def merger_worker(col_name,dest_name,ids,mapper,upsert,batch_num):
    try:
        src = mongo.get_src_db()
        tgt = mongo.get_target_db()
        col = src[col_name]
        #if batch_num == 2:
        #    raise ValueError("oula pa bon")
        dest = DocMongoBackend(tgt,tgt[dest_name])
        cur = doc_feeder(col, step=len(ids), inbatch=False, query={'_id': {'$in': ids}})
        mapper.load()
        docs = mapper.process(cur)
        cnt = dest.update(docs, upsert=upsert)
        return cnt
    except Exception as e:
        logger_name = "build_%s_%s_batch_%s" % (dest_name,col_name,batch_num)
        logger = get_logger(logger_name, btconfig.LOG_FOLDER)
        logger.exception(e)
        exc_fn = os.path.join(btconfig.LOG_FOLDER,"%s.pick" % logger_name)
        pickle.dump(e,open(exc_fn,"wb"))
        logger.info("Exception was dumped in pickle file '%s'" % exc_fn)
        raise


def set_pending_to_build(conf_name=None):
    src_build_config = get_src_build_config()
    qfilter = {}
    if conf_name:
        qfilter = {"_id":conf_name}
    logging.info("Setting pending_to_build flag for configuration(s): %s" % (conf_name and conf_name or "all configuraitons"))
    src_build_config.update(qfilter,{"$set":{"pending_to_build":True}})


class BuilderManager(BaseManager):

    def __init__(self,source_backend_factory=None,
                      target_backend_factory=None,
                      builder_class=None,poll_schedule=None,
                      *args,**kwargs):
        """
        BuilderManager deals with the different builders used to merge datasources.
        It is connected to src_build() via sync(), where it grabs build information
        and register builder classes, ready to be instantiate when triggering builds.
        source_backend_factory can be a optional factory function (like a partial) that
        builder can call without any argument to generate a SourceBackend.
        Same for target_backend_factory for the TargetBackend. builder_class if given
        will be used as the actual Builder class used for the merge and will be passed
        same arguments as the base DataBuilder
        """
        super(BuilderManager,self).__init__(*args,**kwargs)
        self.src_build_config = get_src_build_config()
        self.source_backend_factory = source_backend_factory
        self.target_backend_factory = target_backend_factory
        self.builder_class = builder_class
        self.poll_schedule = poll_schedule
        self.setup_log()
        # check if src_build exist and create it as necessary
        if self.src_build_config.count() == 0:
            logging.debug("Creating '%s' collection (one-time)" % self.src_build_config.name)
            self.src_build_config.database.create_collection(self.src_build_config.name)
            # this is dummy configuration, used as a template
            logging.debug("Creating dummy configuration (one-time)")
            conf = {"_id" : "placeholder",
                    "name" : "placeholder",
                    "doc_type" : "doctypename",
                    "root" : [],
                    "sources" : []}
            self.src_build_config.insert_one(conf)

    def register_builder(self,build_name):
        # will use partial to postponse object creations and their db connection
        # as we don't want to keep connection alive for undetermined amount of time
        # declare source backend
        def create(build_name):
            # postpone config import so app had time to set it up
            # before actual call time
            from biothings import config
            source_backend =  self.source_backend_factory and self.source_backend_factory() or \
                                    partial(backend.SourceDocMongoBackend,
                                            build_config=partial(get_src_build_config),
                                            build=partial(get_src_build),
                                            master=partial(get_src_master),
                                            dump=partial(get_src_dump),
                                            sources=partial(mongo.get_src_db))

            # declare target backend
            target_backend = self.target_backend_factory and self.target_backend_factory() or \
                                    partial(TargetDocMongoBackend,
                                            target_db=partial(mongo.get_target_db))

            # assemble the whole
            klass = self.builder_class and self.builder_class or DataBuilder
            bdr = klass(
                    build_name,
                    source_backend=source_backend,
                    target_backend=target_backend,
                    log_folder=config.LOG_FOLDER)

            return bdr

        self.register[build_name] = partial(create,build_name)

    def setup_log(self):
        self.logger = btconfig.logger

    def __getitem__(self,build_name):
        """
        Return an instance of a builder for the build named 'build_name'
        Note: each call returns a different instance (factory call behind the scene...)
        """
        # we'll get a partial class but will return an instance
        pclass = BaseManager.__getitem__(self,build_name)
        return pclass()

    def configure(self):
        """Sync with src_build_config and register all build config"""
        for conf in self.src_build_config.find():
            self.register_builder(conf["_id"])

    def merge(self, build_name, sources=None, target_name=None, **kwargs):
        """
        Trigger a merge for build named 'build_name'. Optional list of sources can be
        passed (one single or a list). target_name is the target collection name used
        to store to merge data. If none, each call will generate a unique target_name.
        """
        try:
            bdr = self[build_name]
            job = bdr.merge(sources,target_name,job_manager=self.job_manager,**kwargs)
            return job
        except KeyError as e:
            raise BuilderException("No such builder for '%s'" % build_name)

    def list_sources(self,build_name):
        """
        List all registered sources used to trigger a build named 'build_name'
        """
        info = self.src_build_config.find_one({"_id":build_name})
        return info and info["sources"] or []

    def clean_temp_collections(self,build_name,date=None,prefix=''):
        """
        Delete all target collections created from builder named
        "build_name" at given date (or any date is none given -- carefull...).
        Date is a string (YYYYMMDD or regex)
        Common collection name prefix can also be specified if needed.
        """
        target_db = mongo.get_target_db()
        for col_name in target_db.collection_names():
            search = prefix and prefix + "_" or ""
            search += build_name + '_'
            search += date and date + '_' or ''
            pat = re.compile(search)
            if pat.match(col_name) and not 'current' in col_name:
                logging.info("Dropping target collection '%s" % col_name)
                target_db[col_name].drop()

    def poll(self):
        if not self.poll_schedule:
            raise ManagerError("poll_schedule is not defined")
        src_build_config = get_src_build_config()
        @asyncio.coroutine
        def check_pending_to_build():
            confs = [src['_id'] for src in src_build_config.find({'pending_to_build': True}) if type(src['_id']) == str]
            logging.info("Found %d configuration(s) to build (%s)" % (len(confs),repr(confs)))
            for conf_name in confs:
                logging.info("Launch build for '%s'" % conf_name)
                try:
                    self.merge(conf_name)
                except Exception as e:
                    import traceback
                    logging.error("Build for configuration '%s' failed: %s\n%s" % (conf_name,e,traceback.format_exc()))
                    raise
        cron = aiocron.crontab(self.poll_schedule,func=partial(check_pending_to_build),
                start=True, loop=self.job_manager.loop)

