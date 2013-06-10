#from webapp.webapp import settings
from django.conf import settings
import os


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'sismocaracas',
        'USER':'postgres',
        'PASSWORD':'postgres',

    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'sismocaracas2',
        'USER':'funvisis',
        'PASSWORD':'funvisis',
        'HOST':'localhost',
        }
}

if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
