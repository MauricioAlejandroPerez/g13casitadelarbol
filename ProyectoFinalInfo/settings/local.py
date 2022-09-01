from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$6ntm$-0m_gewnd8_xyk829d&nhl26^)vmx#7splbg@(v30j&$'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'proyectofinalinfo',
        'USER': 'Test',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}