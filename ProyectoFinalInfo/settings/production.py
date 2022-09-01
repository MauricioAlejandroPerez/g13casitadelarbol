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
        'USER': 'lcgaqkmlzfcduj',
        'PASSWORD': '5eb2a54a100fd1dfb4762cd9029f410be3fbde9046259ae2cef01619540d653a',
        'HOST': 'ec2-44-194-92-192.compute-1.amazonaws.com',
        'PORT': '5432',
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
