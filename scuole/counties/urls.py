# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.urls import path

from . import views

urlpatterns = [path("", views.CountyListView.as_view(), name="list")]
