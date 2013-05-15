#from webapp.webapp import settings
from django.conf import settings
import os


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(settings.VAR_ROOT, '69grados.com.db'), 
    }
}


if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
