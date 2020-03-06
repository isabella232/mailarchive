# settings/development.py
from .base import *

DEBUG = True

DATA_ROOT = '/a/mailarch/data'

# DJANGO DEBUG TOOLBAR SETTINGS
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
INTERNAL_IPS = get_secret('INTERNAL_IPS')
DEBUG_TOOLBAR_CONFIG = {'INSERT_BEFORE': '<!-- debug_toolbar_here -->'}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 3500

# HAYSTACK SETTINGS
# BaseSignalProcessor does not update the index
# RealtimeSignalProccessor updates the index immediately
# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.BaseSignalProcessor'
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_CONNECTIONS['default']['ENGINE'] = 'mlarchive.archive.backends.custom.ConfigurableElasticSearchEngine'
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://127.0.0.1:9200/'
HAYSTACK_CONNECTIONS['default']['INDEX_NAME'] = 'mail-archive'

# ARCHIVE SETTINGS
ARCHIVE_DIR = os.path.join(DATA_ROOT, 'archive')
CONSOLE_STATS_FILE = os.path.join(DATA_ROOT, 'log', 'console.json')
SERVER_MODE = 'development'

# LOGGING
LOGGING['loggers']['mlarchive']['level'] = 'DEBUG'

ALLOWED_HOSTS = ['.ietf.org', '.amsl.com', '127.0.0.1']
