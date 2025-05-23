"""
Django and project specific settings for usage in production.
Edit this file and adjust the options to your own requirements! You may also set additional options from
https://docs.djangoproject.com/en/1.8/ref/settings/.
"""

# pylint: disable=wildcard-import, unused-wildcard-import
from ctf_gameserver.web.base_settings import *


# Content Security Policy header in the format `directive: [values]`, see e.g
# http://www.html5rocks.com/en/tutorials/security/content-security-policy/ for an explanation
# The initially selected directives should cover most sensitive cases, but still allow YouTube embeds,
# webfonts etc.
CSP_POLICIES = {
    'base-uri': ["'self'"],
    'connect-src': ["'self'"],
    'form-action': ["'self'"],
    'object-src': ["'none'"],
    'script-src': ["'self'"],
    'style-src': ["'self'"]
}

# Set to True if your site is available exclusively through HTTPS and not via plaintext HTTP
HTTPS = False


# Your database settings
# See https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'gameserver-postgres',
        'PORT': 5432,
        'NAME': 'ctf-gameserver',
        'USER': 'ctf-gameserver',
        'PASSWORD': '9iyzXY6pMYzRvXZi',
        'CONN_MAX_AGE': 60
    }
}

# Your cache configuration
# See https://docs.djangoproject.com/en/1.8/topics/cache/#setting-up-the-cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': 'gameserver-memcached:11211',
        'TIMEOUT': 60
    }
}

# Settings for the SMTP server that will be used to send email messages
# See https://docs.djangoproject.com/en/1.8/ref/settings/#email-host and other options
# EMAIL_HOST = ''
# EMAIL_PORT = 25
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# # See https://docs.djangoproject.com/en/1.8/ref/settings/#email-use-tls
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = False

# # Sender address for messages sent by the gameserver
# DEFAULT_FROM_EMAIL = ''
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'ctf-gameserver.web@localhost'

# Filesystem path where user-uploaded files are stored
# This directory must be served by the web server under the path defined by MEDIA_URL in 'base_settings.py'
# ("/uploads" by default)
MEDIA_ROOT = '/uploads'

# The backend used to store user sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# A long, random string, which you are supposed to keep secret
SECRET_KEY = '4HqT2rlhn4efX7jZ2d8MkCBzgRLO0t33udFoqi5YEt72VeHhBv3pTI6pUIGsCPZP'

# Insert all hostnames your site is available under
# See https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# The name of the time zone (i.e. something like "Europe/Berlin") in which dates should be displayed
# See https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for a list of valid options
TIME_ZONE = 'Europe/Vienna'

# First day of the week: 0 means Sunday, 1 means Monday and so on
FIRST_DAY_OF_WEEK = 1

# When using Graylog for checker logging, base URL for generating links to log searches
# Probably either "http://<host>:<port>/search" or "http://<host>:<port>/streams/<stream>/search"
#GRAYLOG_SEARCH_URL = 'http://localhost:9000/search'


# You should not have to edit anything below this line

# # Set up logging to syslog
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'syslog': {
#             'class': 'logging.handlers.SysLogHandler',
#             'address': '/dev/log'
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['syslog'],
#             'level': 'WARNING'
#         }
#     }
# }

DEBUG = False

if HTTPS:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
