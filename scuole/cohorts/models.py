# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models


class CohortsYear(models.Model):
    name = models.CharField(max_length=4)


class CohortsBase(models.Model):
    ethnicity = models.CharField(max_length=15)
    gender = models.CharField(max_length=15)
    economic_status = models.CharField(max_length=30)
    year = models.IntegerField()

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
    bacc = models.IntegerField()
    bacc_acc = models.IntegerField()
    bacc_cert = models.IntegerField()
    assoc = models.IntegerField()
    accoc_cert = models.IntegerField()
    cert = models.IntegerField()

    class Meta:
        abstract = True
