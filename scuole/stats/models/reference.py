# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

ACCOUNTABILITY_YEAR_OVERRIDE = "2024-2025"

class ReferenceBase(models.Model):
    """
    An abstract model representing reference data tracked across all entities
    in TEA data. Meant to be used in addition to StatsBase by other apps for
    establishing their stats models.

    """

    MET_STANDARD = "M"
    # Removed this below because it was giving schools with A grades a "Met alternative standard" label, can add this back in if it causes problems
    MET_ALTERNATIVE_STANDARD = "A"
    MET_ALTERNATIVE_STANDARD_AF = "T"
    IMPROVEMENT_REQUIRED = "I"
    NOT_RATED_X = "X"
    NOT_RATED_Z = "Z"
    NOT_RATED_DATA_INTEGRITY_ISSUE = "Q"
    NOT_RATED_ANNEXATION = "T"
    NOT_RATED_HARVEY = "H"
    NOT_RATED_PAIRED = "P"
    NOT_RATED_DISASTER = "DD"
    NOT_RATED_REVIEW = "R"
    NOT_RATED_SB1365 = "SB"

    RATING_CHOICES = (
        (MET_STANDARD, "Met standard"),
        # (MET_ALTERNATIVE_STANDARD, "Met alternative standard"),
        (MET_ALTERNATIVE_STANDARD_AF, "Met alternative standard"),
        (IMPROVEMENT_REQUIRED, "Improvement required"),
        (NOT_RATED_X, "Not rated"),
        (NOT_RATED_Z, "Not rated"),
        (NOT_RATED_DATA_INTEGRITY_ISSUE, "Not rated (data integrity issue)"),
        (NOT_RATED_ANNEXATION, "Not rated (Annexed)"),
        (NOT_RATED_HARVEY, "Not rated (Harvey provision)"),
        (NOT_RATED_PAIRED, "Not rated (Paired campus)"),
        (NOT_RATED_DISASTER, "Not Rated: Declared State of Disaster"),
        (NOT_RATED_REVIEW, "Not Rated: Data Under Review"),
        (NOT_RATED_SB1365, "Not Rated: Senate Bill 1365"),
        (NOT_RATED_SB1365, "Not Rated: SB 1365"),
        ("", None),
    )

    RATING_MATCH = {
        "Met Standard": MET_STANDARD,
        "Met Alternative Standard": MET_ALTERNATIVE_STANDARD_AF,
        "Improvement Required": IMPROVEMENT_REQUIRED,
        "Not Rated": NOT_RATED_X,
        "Not Rated: Annexation": NOT_RATED_ANNEXATION,
        "Not Rated: Harvey Provision": NOT_RATED_HARVEY,
        "Not Rated: Paired Campus": NOT_RATED_PAIRED,
        "Not Rated: Declared State of Disaster": NOT_RATED_DISASTER,
        "Not Rated: Data Under Review": NOT_RATED_REVIEW,
        "Not Rated: Senate Bill 1365": NOT_RATED_SB1365,
        "Not Rated: SB 1365": NOT_RATED_SB1365,
    }

    RATING_MATCH_LEGACY = {
        "Met Standard": MET_STANDARD,
        "Met Alternative Standard": "A",
        "Improvement Required": IMPROVEMENT_REQUIRED,
        "Not Rated": NOT_RATED_X,
        "Not Rated: Annexation": NOT_RATED_ANNEXATION,
    }

    uses_legacy_ratings = models.BooleanField(
        help_text="This Stats model uses the old accountability system", default=True
    )

    # latest accountability ratings
    accountability_rating = models.CharField(
        _("Accountability rating from the latest year"),
        max_length=2,
        choices=RATING_CHOICES,
        blank=True,
        default="",
    )

    # Only exists for schools with A-F
    student_achievement_rating = models.CharField(
        _("Student achievement rating from the latest year"),
        max_length=2,
        choices=RATING_CHOICES,
        blank=True,
        default="",
    )

    school_progress_rating = models.CharField(
        _("School progress rating from the latest year"),
        max_length=2,
        choices=RATING_CHOICES,
        blank=True,
        default="",
    )

    closing_the_gaps_rating = models.CharField(
        _("Closing the gaps rating from the latest year"),
        max_length=2,
        choices=RATING_CHOICES,
        blank=True,
        default="",
    )

    # accountability ratings from 2018-19
    accountability_rating_18_19 = models.CharField(
        _("Accountability rating from 2018-19"),
        max_length=2,
        choices=RATING_CHOICES,
        blank=True,
        default="",
        null=True,
    )

    student_achievement_rating_18_19 = models.CharField(
        _("Student achievement rating from 2018-19"),
        max_length=2,
        choices=RATING_CHOICES,
        blank=True,
        default="",
        null=True,
    )

    school_progress_rating_18_19 = models.CharField(
        _("School progress rating from 2018-19"),
        max_length=2,
        choices=RATING_CHOICES,
        blank=True,
        default="",
        null=True,
    )

    closing_the_gaps_rating_18_19 = models.CharField(
        _("Closing the gaps rating from 2018-19"),
        max_length=2,
        choices=RATING_CHOICES,
        blank=True,
        default="",
        null=True,
    )

    class Meta:
        abstract = True

    # handling the year shown next the intro `Accountability rating` header
    def get_smart_rating_header_display(self, field_name):
        if ACCOUNTABILITY_YEAR_OVERRIDE:
            return ACCOUNTABILITY_YEAR_OVERRIDE
    
        display_fn = getattr(self, f"get_{field_name}_display")

        if display_fn() is None:
            return getattr(self, "year")
        else:
            return '2018-2019'

    @property
    def smart_accountability_rating_header_display(self):
        return self.get_smart_rating_header_display("accountability_rating_18_19")
    
    
    # handling which accountability rating is shown
    def get_smart_rating_display(self, field_name):
        display_fn = getattr(self, f"get_{field_name}_display")

        # if the school or district does not have a 2018-19 rating, use the latest rating
        if display_fn() is None:
            display_fn = getattr(self, f"get_{field_name.replace('_18_19', '')}_display")

        # if the old accountability system is used
        if self.uses_legacy_ratings:
            return display_fn()
        else:
            value = getattr(self, field_name)

            if value == self.MET_ALTERNATIVE_STANDARD_AF:
                return value

            return display_fn()
    
    @property
    def smart_accountability_rating_display(self):
        return self.get_smart_rating_display("accountability_rating_18_19")

    @property
    def smart_student_achievement_rating_display(self):
        return self.get_smart_rating_display("student_achievement_rating_18_19")

    @property
    def smart_school_progress_rating_display(self):
        return self.get_smart_rating_display("school_progress_rating_18_19")

    @property
    def smart_closing_the_gaps_rating_display(self):
        return self.get_smart_rating_display("closing_the_gaps_rating_18_19")
