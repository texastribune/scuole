# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class State(models.Model):
    name = models.CharField(help_text="State name", max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name
