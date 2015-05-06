from __future__ import absolute_import, unicode_literals

from .base import *

#######################
# DEBUG CONFIGURATION #
#######################

DEBUG = True

TEMPLATE_DEBUG = DEBUG

########################
# SECRET CONFIGURATION #
########################

SECRET_KEY = env('SECRET_KEY', 'this_is_my_secret_key')

#######################
# CACHE CONFIGURATION #
#######################

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

######################################
# DJANGO DEBUG TOOLBAR CONFIGURATION #
######################################

INSTALLED_APPS += ('debug_toolbar', )
