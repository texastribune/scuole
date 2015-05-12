# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.states.models import State


@python_2_unicode_compatible
class County(models.Model):
    name = models.CharField(help_text="County name", max_length=100)
    slug = models.SlugField()
    fips = models.CharField(help_text="County fips code", max_length=3)
    state = models.ForeignKey(State, related_name='counties')

    def __str__(self):
        return self.name
