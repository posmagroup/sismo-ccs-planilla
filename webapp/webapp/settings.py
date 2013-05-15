# Django settings for webapp project.
# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *


#============================================================
# Generic Django Settings
#============================================================

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'webapp.wsgi.application'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Make this unique, and don't share it with anybody.
SECRET_KEY = 's%)_d4#d=7j-5^9=(^fgg8%z00f*p(_q!12c+b_6qgek&amp;_@p^_'

#============================================================
# Calculation of directories relative to the module location
#============================================================

import os, sys


PROJECT_DIR, SITE_ROOT = os.path.split(
    os.path.dirname(os.path.realpath(__file__))
)


VAR_ROOT = os.path.join(os.path.split(PROJECT_DIR)[0], 'var')
if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

#============================================================
# Time and Language Settings.
#============================================================

TIME_ZONE = 'America/Caracas'
LANGUAGE_CODE = 'es-ve'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = False


#============================================================
# Project URLs and media Settings.
#============================================================

ROOT_URLCONF = 'webapp.urls'

LOGIN_URL = 'login'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = ''

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(VAR_ROOT,  'static')

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
IMPERAVI_UPLOAD_PATH = MEDIA_ROOT


if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

if not os.path.exists(MEDIA_ROOT):
    os.mkdir(MEDIA_ROOT)


STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
    #os.path.join(VAR_ROOT, 'static', 'CACHE'),
    )


print STATIC_ROOT

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',
    )



#============================================================
# Template Settings
#============================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
    )

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )

TEMPLATE_CONTEXT_PROCESSORS += (
    # 'Custom context processors here',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',

    )

#============================================================
# Middleware
#============================================================

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

#==============================================================================
# Third-Party Apps
#==============================================================================

#===============================================================================
# COMPRESSOR Settings
#===============================================================================

COMPRESS_ROOT = STATIC_ROOT

COMPRESS_ENABLED = True

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    ]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.SlimItFilter',
    'compressor.filters.jsmin.JSMinFilter'
]


#=====================================================================
# Database. Default settings ONLY. All development settings must be 
# defined in conf.local.settings
#=====================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'portal69grados',                      # Or path to database file if using sqlite3.
        'USER': '69grados',                      # Not used with sqlite3.
        'PASSWORD': '69grados123',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

#==========================================================================
# Applications settings
#==========================================================================

AUTH_PROFILE_MODULE = 'usuario.UserProfile'

#################### configuration email.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = ''

#==========================================================================
# Installed Apps. All dev-only apps must be defined in conf.local.settings
#==========================================================================

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # Third Party Apps
    'south',
    'compressor',
    'imperavi',

    # Project Apps.
    'apps.usuario',
    'apps.inspeccion',
    # Admin
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    )

#============================================================
# Logging
#============================================================

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}

#============================================================
# Local Settings
#============================================================


import sys

try:
    from webapp.conf.local.settings import *
except sys.exc_info()[0], e:
    print """
    NO ESTA 
    LLEGANDO
    AL
    LOCAL
    """
    raise
    pass
