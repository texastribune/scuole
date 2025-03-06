# -*- coding: utf-8 -*-

import dj_database_url
from .base import *  # noqa

#######################
# DEBUG CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-DEBUG
DEBUG = env('DJANGO_DEBUG', True)

##########################
# SECURITY CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.8/ref/settings/#secret-key
# This key should only be used for development and testing!
SECRET_KEY = env('SECRET_KEY', 'this_is_my_development_key')

######################
# HOST CONFIGURATION #
######################

# https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['*']

##########################
# DATABASE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(default='postgis://localhost/scuole')
}

# https://docs.djangoproject.com/en/1.8/topics/db/transactions/#tying-transactions-to-http-requests
DATABASES['default']['ATOMIC_REQUESTS'] = True

##########################
# TEMPLATE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(APPS_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'scuole.custom_processors.district_campus_count',
            ],
        },
    },
]

######################################
# DJANGO DEBUG TOOLBAR CONFIGURATION #
######################################

if not env('DISABLE_DEBUG_TOOLBAR', False):
    INSTALLED_APPS += (
        'debug_toolbar',
    )

    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INTERNAL_IPS = ['127.0.0.1']

###################################
# DJANGO EXTENSIONS CONFIGURATION #
###################################

INSTALLED_APPS += (
    'django_extensions',
)

#################
# SERVICE DEBUG #
#################
# RUNSERVER_PLUS_EXTRA_ARGS = ['--nothreading', '--noreload', '0.0.0.0:8000']
