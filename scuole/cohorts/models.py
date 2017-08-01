# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models


class CohortsYear(models.Model):
    name = models.CharField(max_length=4)


class CohortsBase(models.Model):

    FEMALE = 'F'
    MALE = 'M'

    GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male')
    )

    WHITE = 'W'
    HISPANIC = 'H'
    AFRICAN_AMERICAN = 'B'
    OTHERS = 'O'

    ETHNICITY_CHOICES = (
        (WHITE, 'White'),
        (HISPANIC, 'Hispanic'),
        (AFRICAN_AMERICAN, 'African American'),
        (OTHERS, 'Others')
    )

    ECONOMICALLY_DISADVANTAGED = 'ED'
    NOT_ECONOMICALLY_DISADVANTAGED = 'NED'

    ECON_CHOICES = (
        (ECONOMICALLY_DISADVANTAGED, 'Economically Disadvantaged'),
        (NOT_ECONOMICALLY_DISADVANTAGED, 'Not Economically Disadvantaged')
    )

    gender = models.CharField(
        'Gender', max_length=1, choices=GENDER_CHOICES, null=True)
    ethnicity = models.CharField(
        'Ethnicity', max_length=16, choices=ETHNICITY_CHOICES, null=True)
    economic_status = models.CharField(
        'Economic status', max_length=1, choices=ECON_CHOICES, null=True)

    enrolled_8th = models.IntegerField()
    enrolled_9th = models.IntegerField()
    enrolled_9th_percent = models.FloatField()
    enrolled_10th = models.IntegerField()
    enrolled_10th_percent = models.FloatField()
    lessthan_10th_enrolled = models.IntegerField()
    lessthan_10th_enrolled_percent = models.FloatField()

    graduated = models.IntegerField()
    graduated_percent = models.FloatField()

    enrolled_4yr = models.IntegerField()
    enrolled_4yr_percent = models.FloatField()
    enrolled_2yr = models.IntegerField()
    enrolled_2yr_percent = models.FloatField()
    total_enrolled = models.IntegerField()
    total_enrolled_percent = models.FloatField()

    total_degrees = models.IntegerField()
    total_degrees_percent = models.FloatField()
    bacc = models.IntegerField(null=True, blank=True)
    bacc_acc = models.IntegerField(null=True, blank=True)
    bacc_cert = models.IntegerField(null=True, blank=True)
    assoc = models.IntegerField(null=True, blank=True)
    accoc_cert = models.IntegerField(null=True, blank=True)
    cert = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True
