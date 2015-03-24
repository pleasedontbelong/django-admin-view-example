from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '$',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG = True

TEMPLATE_DEBUG = True
