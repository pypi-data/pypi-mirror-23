''' Functions to return versions of things. '''
from subprocess import check_output
from io import StringIO
from contextlib import redirect_stdout
import pip
import os, sys
import biothings

def get_python_version():
    ''' Get a list of python packages installed and their versions. '''
    so = StringIO()

    with redirect_stdout(so):
        pip.main(['freeze'])

    if so.getvalue():
        return so.getvalue().strip('\n').split('\n')

    return []

def get_biothings_commit():
    ''' Gets the biothings commit information. '''
    try:
        with open(os.path.join(os.path.dirname(biothings.__file__), '.git-info'), 'r') as f:
            lines = [l.strip('\n') for l in f.readlines()]
        return {'repository-url': lines[0], 'commit-hash': lines[1], 'master-commits': lines[2], 'version': biothings.get_version()}
    except:
        return {'repository-url': '', 'commit-hash': '', 'master-commits': '', 'version': biothings.get_version()}


def get_repository_information(app_dir=None):
    ''' Get the repository information for the local repository, if it exists. '''
    if not app_dir:
        return {'repository-url': '', 'commit-hash': ''}

    try:
        commit_hash = check_output("cd {};git rev-parse HEAD".format(os.path.abspath(app_dir)), 
                        shell=True).decode('utf-8').strip('\n')
    except:
        commit_hash = ''

    try:
        repository_url = check_output("cd {};git config --get remote.origin.url".format(os.path.abspath(app_dir)), 
                        shell=True).decode('utf-8').strip('\n')
    except:
        repository_url = ''

    return {'repository-url': repository_url, 'commit-hash': commit_hash}

def get_python_exec_version():
    return {
            'version' : sys.version,
            'version_info' : {
                "major" : sys.version_info[0],
                "minor" : sys.version_info[1],
                "micro" : sys.version_info[2]
                }
            }

def get_software_info(app_dir=None):
    return {
            'python-package-info': get_python_version(),
            'codebase': get_repository_information(app_dir=app_dir),
            'biothings': get_biothings_commit(),
            'python-info' : get_python_exec_version(),
            }
