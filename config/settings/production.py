# -*- coding: utf-8 -*-

from .base import *

import dj_database_url

#######################
# DEBUG CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-DEBUG
DEBUG = env('DJANGO_DEBUG', False)

##########################
# DATABASE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config()
}

# https://docs.djangoproject.com/en/1.8/topics/db/transactions/#tying-transactions-to-http-requests
DATABASES['default']['ATOMIC_REQUESTS'] = True

# https://docs.djangoproject.com/en/1.9/ref/databases/#persistent-connections
# https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-CONN_MAX_AGE
DATABASES['default']['CONN_MAX_AGE'] = 60

#######################
# CACHE CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/1.8/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

##########################
# TEMPLATE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(APPS_DIR, 'templates')],
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ])
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#############################
# STATIC FILE CONFIGURATION #
#############################

# https://docs.djangoproject.com/en/1.8/ref/settings/#staticfiles-storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

######################
# HOST CONFIGURATION #
######################

# https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['.texastribune.org']

#########################
# LOGGING CONFIGURATION #
#########################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

##########################
# SECURITY CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.8/ref/settings/#secret-key
# This key should only be used for development and testing!
SECRET_KEY = env('SECRET_KEY')

# https://docs.djangoproject.com/en/1.8/ref/settings/#secure-content-type-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#x-frame-options
X_FRAME_OPTIONS = 'DENY'

# https://docs.djangoproject.com/en/1.8/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


########################
# SENTRY CONFIGURATION #
########################

# https://getsentry.com/for/django/
RAVEN_CONFIG = {
    'dsn': env('SENTRY_DSN', 'None'),
    'site': env('SENTRY_SITE', 'Public Schools')
}

INSTALLED_APPS = INSTALLED_APPS + (
    'raven.contrib.django.raven_compat',
)

############################
# MIDDLEWARE CONFIGURATION #
############################

MIDDLEWARE += ('whitenoise.middleware.WhiteNoiseMiddleware',)
