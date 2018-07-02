# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from . import views
from scuole.campuses.views import CampusDetailView

app_name = 'districts'

urlpatterns = [
    url(r'^$', views.DistrictListView.as_view(), name='list'),
    url(r'^(?P<district_slug>[\w-]+)/(?:(?P<district_year>[0-9]{4}-[0-9]{4})/)?', include([
        url(r'^$', views.DistrictDetailView.as_view(), name='detail'),
        url(r'^(?P<slug>[\w-]+)/(?:(?P<campus_year>[0-9]{4}-[0-9]{4})/)?$',
            CampusDetailView.as_view(), name='campus'),
    ]))
]
