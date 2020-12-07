DJANGO_DEFINED = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # required for allauth
]

ALLAUTH = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.facebook',
]

TJET_APPS = [
    'agritjet',
]

INSTALLED_APPS = DJANGO_DEFINED + ALLAUTH + TJET_APPS