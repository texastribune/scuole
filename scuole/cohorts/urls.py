# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from .views import (
    CountyCohortsDetailView,
    RegionCohortsDetailView,
    StateCohortsDetailView,
)

urlpatterns = [
    url(r'^$',
        StateCohortsDetailView.as_view(), name='landing'),
    url(r'^states/(?P<slug>[\w-]+)/$',
        StateCohortsDetailView.as_view(), name='states'),
    url(r'^regions/(?P<slug>[\w-]+)/$',
        RegionCohortsDetailView.as_view(), name='regions'),
    url(r'^counties/(?P<slug>[\w-]+)/$',
        CountyCohortsDetailView.as_view(), name='counties'),
]
