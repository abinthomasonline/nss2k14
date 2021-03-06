# Django settings for bloodline_server project.

#Project path
import os, sys, random
import django
from django.core.exceptions import SuspiciousOperation

gettext = lambda s: s

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
PYTHON_VERSION = '%s.%s' % sys.version_info[:2]
DJANGO_VERSION = django.get_version()

DEBUG = False  # Is in Specific Settings also
TEMPLATE_DEBUG = DEBUG
DAJAXICE_DEBUG = DEBUG

ADMINS = ( # People who receive admin emails
#    ('Abdeali J Kothari', "abdealikothari@gmail.com"),
#    ('Deepak', "deepak.vk.1994@gmail.com"),
#    ('Gowtham V', "gowtham.vg.7@gmail.com"),
)
MANAGERS = ADMINS

# >>>>>>>>>> Moved to SpecificSettings.py
DATABASES = {}
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': '',                      # Or path to database file if using sqlite3.
#         'USER': '',                      # Not used with sqlite3.
#         'PASSWORD': '',                  # Not used with sqlite3.
#         'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#     }
# }

#Absolute URL where the site has been hosted. Don't forget the trailing slash.
SITE_URL = 'http://nss.iitm.ac.in'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Kolkata'
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
DATE_FORMAT = 'N j, Y'
DATETIME_FORMAT = 'P, N j, Y'
TIME_FORMAT = '%H:%M'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, 'files', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, 'files', 'static-files'))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'files', 'static'), # Custon static files
    os.path.join(PROJECT_PATH, 'misc', 'dajax', 'static', 'dajax'), # Dajax static files
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    "misc.dajaxice.finders.DajaxiceFinder", # Dajaxice static finder
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*t$3zqdy@sa&amp;2v3&amp;(h*m!^843+*%a5u&amp;+g4#o^m!gwt^)jxi^8'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Mobile checker from django_user_agents
    #'django_user_agents.middleware.UserAgentMiddleware',
)

ROOT_URLCONF = 'configs.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'configs.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'templates'), # Custom templates
    # os.path.join(PROJECT_PATH, 'misc', 'dajaxice', 'templates'), # Dajaxice templates
)

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    # For humanized dates
    'django.contrib.humanize',
)
THIRD_PARTY_APPS = (
    # South
    'south',
    'south_admin',
    #TastyPie for the RESTFUL API
    # 'tastypie',
    # Mobile checker
    # 'django_user_agents',
    # For template form field changes in template
    'widget_tweaks',
)

NSS_APPS = (
    # Dajax(ice) for async requests
    'misc.dajaxice',
    'misc.dajax',    
    # Our apps
    'apps.nss',
    'apps.accounts',
    'apps.events',
    'misc',
)
INSTALLED_APPS = THIRD_PARTY_APPS + NSS_APPS + DJANGO_APPS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

# To disable suspicious operation error messages
def skip_suspicious_operations(record):
    if record.exc_info:
        exc_value = record.exc_info[1]
        if isinstance(exc_value, SuspiciousOperation):
            return False
    return True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        # Define filter for suspicious operations
        'skip_suspicious_operations': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': skip_suspicious_operations,
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false', 'skip_suspicious_operations'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'misc.dajaxice': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'misc.dajaxice.DajaxiceRequest': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },

    }
}

"""
# Cache backend is optional, but recommended to speed up user agent parsing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
"""

#Authentication Profile
AUTH_PROFILE_MODULE = 'apps.accounts.UserProfile'

# Important urls
LOGIN_URL          = 'apps.nss.views.home'
LOGIN_REDIRECT_URL = 'apps.nss.views.home'
LOGIN_ERROR_URL    = '/login-error/'

#Template context processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',

    #I added these.
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.csrf',

)

# Guardian settings - permissions
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'apps.accounts.backends.RootBackend', # custom default password
)
ROOT_PASSWORD = "pbkdf2_sha256$12000$IzXBCj63hXv6$Kc1WwdQdQX7EqHCUzg9OnrFbZoD5lVSMgczUIYZkqmA="
ANONYMOUS_USER_ID = -1

# Email settings
EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = 'NSS IITM <noreply@nss.iitm.ac.in>'
EMAIL_HOST_USER = 'noreply@nss.iitm.ac.in'
# EMAIL_HOST_PASSWORD = ''

# Captcha settings - django-simple-captcha
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_FOREGROUND_COLOR = '#000000'
CAPTCHA_FILTER_FUNCTIONS = ('captcha.helpers.post_smooth',)
CAPTCHA_NOISE_FUNCTIONS = ()#('captcha.helpers.noise_dots','captcha.helpers.noise_arcs',)
CAPTCHA_FONT_SIZE = 40
CAPTCHA_LETTER_ROTATION = None

# Mobi ignore list fo mobile devices
MOBI_USER_AGENT_IGNORE_LIST = [] # Example : ['ipad'] will ignore ipads
MOBI_DETECT_TABLET = False # Set to True to have another variable request.tablet 
#MOBI_REDIRECT_URL = "http://nss.iitm.ac.in/mobile"

# Admin form and bootstrapping
ADAPTOR_INPLACEEDIT = {}
if 'inplaceeditform_extra_fields' in INSTALLED_APPS:
    ADAPTOR_INPLACEEDIT['tiny'] = 'inplaceeditform_extra_fields.fields.AdaptorTinyMCEField'
    # You can add the other adaptors of inplaceeditform_extra_fields
    # https://pypi.python.org/pypi/django-inplaceedit-extra-fields#installation
if 'bootstrap3_datetime' in INSTALLED_APPS:
    ADAPTOR_INPLACEEDIT['date'] = 'inplaceeditform_bootstrap.fields.AdaptorDateBootStrapField'
    ADAPTOR_INPLACEEDIT['datetime'] = 'inplaceeditform_bootstrap.fields.AdaptorDateTimeBootStrapField'
    ADAPTOR_INPLACEEDIT['date_bootstrap'] = 'inplaceeditform_bootstrap.fields.AdaptorDateBootStrapField'
    ADAPTOR_INPLACEEDIT['datetime_bootstrap'] = 'inplaceeditform_bootstrap.fields.AdaptorDateTimeBootStrapField'
