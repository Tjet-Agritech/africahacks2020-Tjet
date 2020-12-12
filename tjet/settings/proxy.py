import os

from .base import *
from .installed import *

print("using local proxy")

PROXY_PSW = os.getenv("PROXY_PSW")
PROXY_USER = os.getenv("PROXY_USER")
PROXY_DB_NAME = os.getenv("PROXY_DB_NAME", 'production')
PROXY_PORT = os.getenv('PROXY_PORT')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': PROXY_DB_NAME,
        'USER': PROXY_USER,
        'PASSWORD': PROXY_PSW,
        'HOST': '127.0.0.1',
        'PORT': PROXY_PORT,
    }
}
