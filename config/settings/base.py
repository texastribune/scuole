"""
Django settings for scuole project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from __future__ import absolute_import, unicode_literals
from os import environ, path

import dj_database_url

from django.core.exceptions import ImproperlyConfigured

###########
# HELPERS #
###########


def env(setting, default=None):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        if default is not None:
            return default
        else:
            error_msg = ('The {} env variable was not found '
                         'and no default was set!').format(setting)
            raise ImproperlyConfigured(error_msg)

######################
# PATH CONFIGURATION #
######################

# This file
BASE_FILE = path.abspath(__file__)

# Absolute filesystem path to the project directory
ROOT_DIR = path.abspath(path.join(path.dirname(BASE_FILE), '..', '..'))

# Absolute filesystem path to the Django project's app folder
APPS_DIR = path.join(ROOT_DIR, 'scuole')

#######################
# DEBUG CONFIGURATION #
#######################

DEBUG = False

TEMPLATE_DEBUG = DEBUG

#####################
# APP CONFIGURATION #
#####################

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (

)

LOCAL_APPS = (
    'scuole.counties',
    'scuole.districts',
    'scuole.regions',
    'scuole.states',
)

# https://docs.djangoproject.com/en/1.8/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

############################
# MIDDLEWARE CONFIGURATION #
############################
# https://docs.djangoproject.com/en/1.8/topics/http/middleware/

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

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
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

##########################
# DATABASE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default':  dj_database_url.config(default='postgres://localhost/scuole')
}

DATABASES['default']['ATOMIC_REQUESTS'] = True

#############################
# STATIC FILE CONFIGURATION #
#############################

# https://docs.djangoproject.com/en/1.8/ref/settings/#static-root
STATIC_ROOT = path.join(APPS_DIR, 'assets')

# https://docs.djangoproject.com/en/1.8/ref/settings/#static-url
STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/1.8/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    path.join(APPS_DIR, 'static'),
)

# https://docs.djangoproject.com/en/1.8/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

############################
# MEDIA FILE CONFIGURATION #
############################

# https://docs.djangoproject.com/en/1.8/ref/settings/#media-root
MEDIA_ROOT = path.join(APPS_DIR, 'media')

# https://docs.djangoproject.com/en/1.8/ref/settings/#media-url
MEDIA_URL = '/media/'

#####################
# URL CONFIGURATION #
#####################

ROOT_URLCONF = 'config.urls'

# https://docs.djangoproject.com/en/1.8/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

#########################
# GENERAL CONFIGURATION #
#########################

# https://docs.djangoproject.com/en/1.8/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

# https://docs.djangoproject.com/en/1.8/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#use-tz
USE_TZ = True

#########################
# GENERAL CONFIGURATION #
#########################

DATA_FOLDER = env('DATA_FOLDER', path.join(ROOT_DIR, 'data'))
