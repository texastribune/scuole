# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.states.models import State


@python_2_unicode_compatible
class County(models.Model):
    name = models.CharField('County name', max_length=100)
    slug = models.SlugField()
    fips = models.CharField('County FIPS place code', max_length=3)
    state = models.ForeignKey(State, related_name='counties')

    class Meta:
        verbose_name_plural = 'counties'

    def __str__(self):
        return self.name
