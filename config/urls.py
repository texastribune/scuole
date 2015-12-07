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
from django.contrib import admin
from django.views import defaults
from django.views.generic import TemplateView

from scuole.core.views import (AboutView, AcceptRedirectView, LookupView,
                               SearchView)

urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name='landing.html'), name='landing'),
    url(r'^districts/', include(
        'scuole.districts.urls', namespace='districts')),
    url(r'^states/', include(
        'scuole.states.urls', namespace='states')),
    url(r'^search/', SearchView.as_view(), name='search'),
    url(r'^lookup/', LookupView.as_view(), name='lookup'),
    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^redirect/', AcceptRedirectView.as_view(), name='redirect'),
    url(r'^admin/', include(admin.site.urls)),
]

# Test pages normally not reachable when DEBUG = True
if settings.DEBUG:
    urlpatterns += [
        url(r'^400/$', defaults.bad_request),
        url(r'^403/$', defaults.permission_denied),
        url(r'^404/$', defaults.page_not_found),
        url(r'^500/$', defaults.server_error),
    ]
