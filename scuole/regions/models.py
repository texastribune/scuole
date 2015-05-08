from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.states.models import State


@python_2_unicode_compatible
class Region(models.Model):
    name = models.CharField(
        help_text='Geographic name for region', max_length=20)
    region_id = models.CharField(help_text='Region identifier', max_length=2)
    state = models.ForeignKey(State, related_name='regions')

    def __str__(self):
        return '{} - {}'.format(self.name, self.region_id)
