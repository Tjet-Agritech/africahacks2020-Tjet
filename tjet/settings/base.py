"""
Django settings for tjet project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
env_path = BASE_DIR / '.env.env'

load_dotenv(dotenv_path=env_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = []

# Application definition

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tjet.urls'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend')

TEMPLATE_DIR = Path(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tjet.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    Path(BASE_DIR, 'static/'),
]

MEDIA_ROOT = Path(BASE_DIR, 'media/')

# SOCIAL AUTH AUTH0 BACKEND CONFIG
SOCIAL_AUTH_TRAILING_SLASH = False
SOCIAL_AUTH_AUTH0_KEY = os.environ.get('AUTH0_CLIENT_ID')
SOCIAL_AUTH_AUTH0_SECRET = os.environ.get('AUTH0_CLIENT_SECRET')
SOCIAL_AUTH_AUTH0_SCOPE = ['openid', 'profile', 'email']
SOCIAL_AUTH_AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
AUDIENCE = None
if os.environ.get('AUTH0_AUDIENCE'):
    AUDIENCE = os.environ.get('AUTH0_AUDIENCE')
else:
    if SOCIAL_AUTH_AUTH0_DOMAIN:
        AUDIENCE = 'https://' + SOCIAL_AUTH_AUTH0_DOMAIN + '/userinfo'
if AUDIENCE:
    SOCIAL_AUTH_AUTH0_AUTH_EXTRA_ARGUMENTS = {'audience': AUDIENCE}
AUTHENTICATION_BACKENDS = {
    'agritjet.auth0backend.Auth0',
    'django.contrib.auth.backends.ModelBackend'
}

LOGIN_URL = '/login/auth0'
LOGIN_REDIRECT_URL = '/'

STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

# debugging
sentry_sdk.init(
    dsn=os.getenv('SENTRY_SDK_DSN'),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True)