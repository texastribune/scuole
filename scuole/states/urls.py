# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.urls import re_path

from . import views

app_name = "states"

urlpatterns = [
    re_path(
        r"^(?P<slug>[\w-]+)/(?:(?P<state_year>[0-9]{4}-[0-9]{4})/)?$",
        views.StateDetailView.as_view(),
        name="detail",
    )
]
