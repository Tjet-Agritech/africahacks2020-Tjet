DJANGO_DEFINED = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # required for allauth
]

AUTH0 = [
    'social_django',
]

TJET_APPS = [
    'agritjet',
    'crispy_forms',
    'django_countries',
]

INSTALLED_APPS = DJANGO_DEFINED + AUTH0 + TJET_APPS