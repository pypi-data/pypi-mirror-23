from biothings.www.api.es.query import ESQuery as DefaultESQuery
from biothings.www.api.es.query_builder import ESQueryBuilder as DefaultESQueryBuilder
from biothings.www.api.es.transform import ESResultTransformer as DefaultESResultTransformer
import re

# *****************************************************************************
# Elasticsearch variables
# *****************************************************************************
# elasticsearch server transport url
ES_HOST = 'localhost:9200'
# timeout for python es client (global request timeout)
ES_CLIENT_TIMEOUT = 120
# elasticsearch index name
ES_INDEX = 'mybiothing_current'
# elasticsearch document type
ES_DOC_TYPE = 'biothing'
# Amount of time a scroll request is kept open
ES_SCROLL_TIME = '1m'
# Size of each scroll request return
ES_SCROLL_SIZE = 1000
# Maximum size of result return
ES_SIZE_CAP = 1000
# Maximum result window => maximum for "from" parameter
ES_RESULT_WINDOW_SIZE_CAP = 10000

# For the userquery folder for this app
USERQUERY_DIR = ''

# default static path, relative to current working dir
# (from where app is launched)
STATIC_PATH = "static"

# api version in the URL patterns and elsewhere
API_VERSION = 'v1'
# project URL routing
APP_LIST = []

# *****************************************************************************
# Subclass of biothings.www.api.es.query_builder.ESQueryBuilder to build
# queries for this app
# *****************************************************************************
ES_QUERY_BUILDER = DefaultESQueryBuilder
# *****************************************************************************
# Subclass of biothings.www.api.es.query.ESQuery to execute queries for this app
# *****************************************************************************
ES_QUERY = DefaultESQuery
# *****************************************************************************
# Subclass of biothings.www.api.es.transform.ESResultTransformer to transform
# ES results for this app
# *****************************************************************************
ES_RESULT_TRANSFORMER = DefaultESResultTransformer

OUTPUT_KEY_ALIASES = {}
#OUTPUT_KEY_ALIASES = {'cadd':'schmadd', 'cadd/gene/ccds_id': 'cces_id'}

# Global default cap for list inputs
LIST_SIZE_CAP = 1000

# TODO: Need to describe
#ANNOTATION_ID_REGEX_LIST = [(re.compile(r'rs[0-9]+', re.I), 'dbsnp.rsid')]
ANNOTATION_ID_REGEX_LIST = []

# USERQUERY KWARGS

# regex to identify a userquery arg
USERQUERY_KWARG_REGEX = re.compile(r'^uq_\w+$')
# transform to use on the userquery arg
USERQUERY_KWARG_TRANSFORM = lambda x: x[3:]

# Keyword Argument Control
# 
# These parameters control which input kwargs go to which kwarg group for each
# endpoint and operation (e.g. query GET, annotation POST, etc).
# This allows explicit grouping of parameters into inputs of the pipeline
# section that they are germane to.
# CONTROL_KWARGS - general category, used for handler parameters (e.g. raw, rawquery)
# ES_KWARGS go directly to the ESQuery function (e.g. fields, size...)
# ESQB_KWARGS are used to instantiate a query builder class
# TRANSFORM_KWARGS are used to instantiate a result transformer class
# 
# keys are parameter names, values are default values.  If value == None, no
# default is inserted.

# For annotation GET endpoint
ANNOTATION_GET_CONTROL_KWARGS = {'raw': {'default': False, 'type': bool}, 
                                 'rawquery': {'default': False, 'type': bool}}
ANNOTATION_GET_ES_KWARGS = {'_source': {'default': None, 'type': list, 'max': 100, 'alias': ['fields', 'filter']}}
ANNOTATION_GET_ESQB_KWARGS = {}
ANNOTATION_GET_TRANSFORM_KWARGS = {'dotfield': {'default': False, 'type': bool}, 
                                   'jsonld': {'default': False, 'type': bool},
                                   '_sorted': {'default': True, 'type': bool}}

# For annotation POST endpoint
ANNOTATION_POST_CONTROL_KWARGS = {'raw': {'default': False, 'type': bool},
                                  'rawquery': {'default': False, 'type': bool},
                                  'ids': {'default': None, 'type': list, 'max': 1000}}
ANNOTATION_POST_ES_KWARGS = {'_source': {'default': None, 'type': list, 'max': 100, 'alias': ['fields', 'filter']}}
ANNOTATION_POST_ESQB_KWARGS = {}
ANNOTATION_POST_TRANSFORM_KWARGS = {'dotfield': {'default': False, 'type': bool},
                                    'jsonld': {'default': False, 'type': bool},
                                    '_sorted': {'default': True, 'type': bool}}

# For query GET endpoint
QUERY_GET_CONTROL_KWARGS = {'raw': {'default': False, 'type': bool},
                            'rawquery': {'default': False, 'type': bool},
                            'q': {'default': None, 'type': str, 
                                'translations': [
                                    #(re.compile(r'chr:', re.I), r'chrom:')
                                ]
                            },
                            'scroll_id': {'default': None, 'type': str},
                            'fetch_all': {'default': False, 'type': bool}}
QUERY_GET_ES_KWARGS = {'_source': {'default': None, 'type': list, 'max': 100, 'alias': ['fields', 'filter']},
                       'from': {'default': None, 'type': int, 'alias': 'skip'},
                       'size': {'default': None, 'type': int, 'alias': 'limit'},
                       'explain': {'default': None, 'type': bool},
                       'aggs': {'default': None, 'type': list, 'max': 10, 'alias': 'facets'},
                       'sort': {'default': None, 'type': list, 'max': 100}}
QUERY_GET_ESQB_KWARGS = {'fetch_all': {'default': False, 'type': bool},
                         'userquery': {'default': None, 'type': str}}
QUERY_GET_TRANSFORM_KWARGS = {'dotfield': {'default': False, 'type': bool},
                              'jsonld': {'default': False, 'type': bool},
                              '_sorted': {'default': True, 'type': bool}}

# For query POST endpoint
QUERY_POST_CONTROL_KWARGS = {'q': {'default': None, 'type': list},
                             'raw': {'default': False, 'type': bool},
                             'rawquery': {'default': False, 'type': bool}}
QUERY_POST_ES_KWARGS = {'_source': {'default': None, 'type': list, 'max': 100, 'alias': ['fields', 'filter']}}
QUERY_POST_ESQB_KWARGS = {'scopes': {'default': None, 'type': list, 'max': 100, 
                            'translations': [

                            ]}}
QUERY_POST_TRANSFORM_KWARGS = {'dotfield': {'default': False, 'type': bool}, 
                               'jsonld': {'default': False, 'type': bool},
                               '_sorted': {'default': True, 'type': bool}}

# For metadata GET endpoint
METADATA_GET_CONTROL_KWARGS = {}
METADATA_GET_ES_KWARGS = {}
METADATA_GET_ESQB_KWARGS = {}
METADATA_GET_TRANSFORM_KWARGS = {'dev': {'default': False, 'type': bool}, 
                                 'search': {'default': None, 'type': str},
                                 'prefix': {'default': None, 'type': str}}

# *****************************************************************************
# Google Analytics Settings
# *****************************************************************************

# Google Analytics Account ID
GA_ACCOUNT = ''

# Turn this to True to start google analytics tracking
GA_RUN_IN_PROD = False

# url for google analytics tracker
GA_TRACKER_URL = 'mybiothing.info'
GA_ACTION_QUERY_GET = 'query_get'
GA_ACTION_QUERY_POST = 'query_post'
GA_ACTION_ANNOTATION_GET = 'biothing_get'
GA_ACTION_ANNOTATION_POST = 'biothing_post'

# for standalone instance tracking
STANDALONE_TRACKING_URL = ''
# dictionary with AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY k,v for standalone user AWS IAM
STANDALONE_AWS_CREDENTIALS = {}
# batch size for standalone tracking (sending requests to AWS lambda)
STANDALONE_TRACKING_BATCH_SIZE = 1000

# override with url for specific project
URL_BASE = 'http://mybiothing.info'

# parameter for JSONP
JSONP_PARAMETER = 'callback'

# Caching behavior
# should caching be disabled by default on handlers?
DISABLE_CACHING = False
CACHE_MAX_AGE = 604800

# Sentry project address
SENTRY_CLIENT_KEY = ''

# JSON-LD PATH
JSONLD_CONTEXT_PATH = ''

# Can turn msgpack functionality off here, will still load msgpack module if available, just won't
# use it to compress requests
ENABLE_MSGPACK = True

LIST_SPLIT_REGEX = re.compile('[\s\r\n+|,]+')

DEFAULT_SCOPES = ['_id']

# path to the git repository for the app-specific code, override
APP_GIT_REPOSITORY = '../'

# ***************************************************************
# * For Hipchat exception logging
# ***************************************************************
HIPCHAT_ROOM=''
HIPCHAT_AUTH_TOKEN=''
HIPCHAT_MESSAGE_COLOR='yellow'
HIPCHAT_AUTO_FROM_SOCKET_CONNECTION=('8.8.8.8', 53) # google DNS server
HIPCHAT_MESSAGE_FORMAT=None
