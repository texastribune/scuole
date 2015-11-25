# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class ReferenceBase(models.Model):
    """
    An abstract model representing reference data tracked across all entities
    in TEA data. Meant to be used in addition to StatsBase by other apps for
    establishing their stats models.

    """

    MET_STANDARD = 'M'
    MET_ALTERNATIVE_STANDARD = 'A'
    IMPROVEMENT_REQUIRED = 'I'
    NOT_RATED_X = 'X'
    NOT_RATED_Z = 'Z'
    NOT_RATED_DUE_TO_DATA_INTEGRITY_ISSUE = 'Q'

    RATING_CHOICES = (
        (MET_STANDARD, _('Met standard')),
        (MET_ALTERNATIVE_STANDARD, _('Met alternative standard')),
        (IMPROVEMENT_REQUIRED, _('Improvement required')),
        (NOT_RATED_X, 'Not rated'),
        (NOT_RATED_Z, 'Not rated'),
        (NOT_RATED_DUE_TO_DATA_INTEGRITY_ISSUE,
            _('Not rated due to data integrity issue')),
    )

    accountability_rating = models.CharField(
        _('Accountability rating'), max_length=1, choices=RATING_CHOICES,
        blank=True, default='')

    class Meta:
        abstract = True
