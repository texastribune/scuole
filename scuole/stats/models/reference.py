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

    MET_STANDARD = "M"
    MET_ALTERNATIVE_STANDARD = "A"
    IMPROVEMENT_REQUIRED = "I"
    NOT_RATED_X = "X"
    NOT_RATED_Z = "Z"
    NOT_RATED_DATA_INTEGRITY_ISSUE = "Q"
    NOT_RATED_ANNEXATION = "T"
    NOT_RATED_HARVEY = "H"

    RATING_CHOICES = (
        (MET_STANDARD, "Met standard"),
        (MET_ALTERNATIVE_STANDARD, "Met alternative standard"),
        (IMPROVEMENT_REQUIRED, "Improvement required"),
        (NOT_RATED_X, "Not rated"),
        (NOT_RATED_Z, "Not rated"),
        (NOT_RATED_DATA_INTEGRITY_ISSUE, "Not rated due to data integrity issue"),
        (NOT_RATED_ANNEXATION, "Not rated due to annexation"),
        (NOT_RATED_HARVEY, "Not rated due to Harvey provision"),
    )

    RATING_MATCH_17_18 = {
        "Met Standard": MET_STANDARD,
        "Met Alternative Standard": MET_ALTERNATIVE_STANDARD,
        "Improvement Required": IMPROVEMENT_REQUIRED,
        "Not Rated": NOT_RATED_X,
        "Not Rated: Annexation": NOT_RATED_ANNEXATION,
        "Not Rated: Harvey Provision": NOT_RATED_HARVEY,
    }

    accountability_rating = models.CharField(
        _("Accountability rating"),
        max_length=1,
        choices=RATING_CHOICES,
        blank=True,
        default="",
    )

    uses_legacy_ratings = models.BooleanField(
        help_text="This Stats model uses the old accountability system", default=True
    )

    # Only exists for schools with A-F
    student_achievement_rating = models.CharField(
        _("Student achievement rating"),
        max_length=1,
        choices=RATING_CHOICES,
        blank=True,
        default="",
    )

    school_progress_rating = models.CharField(
        _("School progress rating"),
        max_length=1,
        choices=RATING_CHOICES,
        blank=True,
        default="",
    )

    closing_the_gaps_rating = models.CharField(
        _("Closing the gaps rating"),
        max_length=1,
        choices=RATING_CHOICES,
        blank=True,
        default="",
    )

    class Meta:
        abstract = True
