from .base import *

import dj_database_url

#######################
# DEBUG CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-DEBUG
DEBUG = env('DEBUG', True)

############################
# SECRET KEY CONFIGURATION #
############################

# https://docs.djangoproject.com/en/1.8/ref/settings/#secret-key
# This key should only be used for development and testing!
SECRET_KEY = env('SECRET_KEY', 'this_is_my_development_key')

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
            ],
        },
    },
]

######################################
# DJANGO DEBUG TOOLBAR CONFIGURATION #
######################################

INSTALLED_APPS += (
    'debug_toolbar',
)
