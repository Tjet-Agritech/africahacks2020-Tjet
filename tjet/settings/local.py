from pathlib import Path
from .base import *
from .installed import *

print("using local")

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}