# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.functional import cached_property

from .managers import CohortQuerySet


class CohortsBase(models.Model):
    FEMALE = 'Female'
    MALE = 'Male'

    GENDER_CHOICES = (
        (FEMALE, 'female'),
        (MALE, 'male'),
    )

    WHITE = 'White'
    HISPANIC = 'Hispanic'
    AFRICAN_AMERICAN = 'African American'
    OTHERS = 'Others'
    UNKNOWN = 'All Ethnicities'

    ETHNICITY_CHOICES = (
        (WHITE, 'white'),
        (HISPANIC, 'hispanic'),
        (AFRICAN_AMERICAN, 'black'),
        (OTHERS, 'other'),
        (UNKNOWN, 'unknown'),
    )

    ECONOMICALLY_DISADVANTAGED = 'Economically Disadvantaged'
    NOT_ECONOMICALLY_DISADVANTAGED = 'Not Economically Disadvantaged'

    ECON_CHOICES = (
        (ECONOMICALLY_DISADVANTAGED, 'economically disadvantaged'),
        (NOT_ECONOMICALLY_DISADVANTAGED, 'not economically disadvantaged')
    )

    gender = models.CharField(
        'Gender', max_length=30, choices=GENDER_CHOICES, blank=True)
    ethnicity = models.CharField(
        'Ethnicity', max_length=30, choices=ETHNICITY_CHOICES, blank=True)
    economic_status = models.CharField(
        'Economic status', max_length=30, choices=ECON_CHOICES, blank=True)

    enrolled_8th = models.IntegerField(null=True)
    enrolled_9th = models.IntegerField(null=True)
    enrolled_10th = models.IntegerField(null=True)
    lessthan_10th_enrolled = models.IntegerField(null=True)

    graduated = models.IntegerField(null=True)

    enrolled_4yr = models.IntegerField(null=True)
    enrolled_2yr = models.IntegerField(null=True)
    enrolled_out_of_state = models.IntegerField(null=True)
    total_enrolled = models.IntegerField(null=True)
    enrolled_wo_record = models.IntegerField(null=True)

    total_degrees = models.IntegerField(null=True)

    objects = CohortQuerySet.as_manager()

    @cached_property
    def percent_graduated(self):
        try:
            return self.graduated / self.enrolled_8th
        except (TypeError, ZeroDivisionError):
            return 'N/A'

    @cached_property
    def percent_enrolled_higher_education(self):
        try:
            return self.total_enrolled / self.enrolled_8th
        except (TypeError, ZeroDivisionError):
            return 'N/A'

    @cached_property
    def percent_completed_higher_education(self):
        try:
            return self.total_degrees / self.enrolled_8th
        except (TypeError, ZeroDivisionError):
            return 'N/A'

    class Meta:
        abstract = True
