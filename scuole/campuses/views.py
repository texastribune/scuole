# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import DetailView

from .models import Campus


class CampusDetailView(DetailView):
    model = Campus
