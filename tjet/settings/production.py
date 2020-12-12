import os
from pathlib import Path

from .base import *
from .installed import INSTALLED_APPS

print('using production')

DEBUG = False
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')

DB_USER_PSW = os.getenv("DB_USER_PSW")
DB_USER_UN = os.getenv("DB_USER_UN")
DB_NAME = os.getenv("DB_NAME", 'production')
INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME")

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER_UN,
        'PASSWORD': DB_USER_PSW,
        'HOST': f'/cloudsql/{INSTANCE_CONNECTION_NAME}',
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = Path(BASE_DIR, 'staticfiles')

DEFAULT_FROM_EMAIL = 'AgritJet <contact@peteranyaogu.me>'
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

ADMINS = (('peter', 'contact@peteranyaogu.me'), )
MANAGERS = ADMINS
