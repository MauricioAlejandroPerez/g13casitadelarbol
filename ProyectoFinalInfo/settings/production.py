from .base import *
import os
import dj_database_url
import django_heroku

# SECURITY WARNING: don't run with debug turned on in production!

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DEBUG = False

DEBUG_PROPAGATE_EXCEPTIONS = True
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_pscyopg2',
        'NAME': 'g13casitadelarbol',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}


DATABASES['default']= dj_database_url.config(conn_max_age=500, ssl_require=True)
django_heroku.settings(locals())

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (  
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE='whitenoise.storage.CompressedStaticFilesStorage'


STATIC_URL = 'https://g13casitadelarbol.herokuapp.com/static/'
MEDIA_URL = 'https://g13casitadelarbol.herokuapp.com/media/' 
