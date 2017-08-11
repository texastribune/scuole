# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models

from .managers import CohortQuerySet


class CohortsBase(models.Model):
    FEMALE = 'Female'
    MALE = 'Male'

    GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )

    WHITE = 'White'
    HISPANIC = 'Hispanic'
    AFRICAN_AMERICAN = 'African American'
    OTHERS = 'Others'

    ETHNICITY_CHOICES = (
        (WHITE, 'White'),
        (HISPANIC, 'Hispanic'),
        (AFRICAN_AMERICAN, 'African American'),
        (OTHERS, 'Others'),
    )

    ECONOMICALLY_DISADVANTAGED = 'Economically Disadvantaged'
    NOT_ECONOMICALLY_DISADVANTAGED = 'Not Economically Disadvantaged'

    ECON_CHOICES = (
        (ECONOMICALLY_DISADVANTAGED, 'Economically Disadvantaged'),
        (NOT_ECONOMICALLY_DISADVANTAGED, 'Not Economically Disadvantaged')
    )

    gender = models.CharField(
        'Gender', max_length=30, choices=GENDER_CHOICES, blank=True)
    ethnicity = models.CharField(
        'Ethnicity', max_length=30, choices=ETHNICITY_CHOICES, blank=True)
    economic_status = models.CharField(
        'Economic status', max_length=30, choices=ECON_CHOICES, blank=True)

    enrolled_8th = models.IntegerField(null=True)
    enrolled_9th = models.IntegerField(null=True)
    enrolled_9th_percent = models.FloatField(null=True)
    enrolled_10th = models.IntegerField(null=True)
    enrolled_10th_percent = models.FloatField(null=True)
    lessthan_10th_enrolled = models.IntegerField(null=True)
    lessthan_10th_enrolled_percent = models.FloatField(null=True)

    graduated = models.IntegerField(null=True)
    graduated_percent = models.FloatField(null=True)

    enrolled_4yr = models.IntegerField(null=True)
    enrolled_4yr_percent = models.FloatField(null=True)
    enrolled_2yr = models.IntegerField(null=True)
    enrolled_2yr_percent = models.FloatField(null=True)
    enrolled_out_of_state = models.IntegerField(null=True)
    enrolled_out_of_state_percent = models.IntegerField(null=True)
    total_enrolled = models.IntegerField(null=True)
    total_enrolled_percent = models.FloatField(null=True)
    enrolled_wo_record = models.IntegerField(null=True)
    enrolled_wo_record_percent = models.FloatField(null=True)

    total_degrees = models.IntegerField(null=True)
    total_degrees_percent = models.FloatField(null=True)
    bacc = models.IntegerField(null=True)
    bacc_acc = models.IntegerField(null=True)
    bacc_cert = models.IntegerField(null=True)
    assoc = models.IntegerField(null=True)
    accoc_cert = models.IntegerField(null=True)
    cert = models.IntegerField(null=True)

    objects = CohortQuerySet.as_manager()

    class Meta:
        abstract = True
