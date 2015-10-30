# -*- coding: utf-8 -*-
"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import TemplateView

from scuole.core.views import SearchView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

public_patterns = [
    url(r'^$', TemplateView.as_view(
        template_name='landing.html'), name='landing'),
    url(r'^districts/', include(
        'scuole.districts.urls', namespace='districts')),
    url(r'^states/', include(
        'scuole.states.urls', namespace='states')),
    url(r'^search/', SearchView.as_view(), name='search'),
]

# Test pages normally not reachable when DEBUG = True
if settings.DEBUG:
    public_patterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    ]

urlpatterns += i18n_patterns(*public_patterns)
