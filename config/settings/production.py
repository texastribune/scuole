from __future__ import absolute_import, unicode_literals
from os import path

import dj_database_url

from .base import *

########################
# SECRET CONFIGURATION #
########################

SECRET_KEY = env('SECRET_KEY')

######################
# HOST CONFIGURATION #
######################

# https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['*']

##########################
# TEMPLATE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.8/topics/templates/#configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            path.join(APPS_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ],
            ],
        },
    },
]

##########################
# DATABASE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES['default'] = dj_database_url.config()

#######################
# CACHE CONFIGURATION #
#######################

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}
