# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Staar20122013Base(models.Model):
    """
    An abstract model representing STAAR test results data commonly
    tracked across all entities in TEA data. Meant to be used with StatsBase
    by other apps for establishing their stats models.

    """

    staar_all_subjects_all_students_met_level_two_count = models.IntegerField(
        _('Number of all students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_african_american_met_level_two_count = models.IntegerField(
        _('Number of African American students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_american_indian_met_level_two_count = models.IntegerField(
        _('Number of American Indian students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_asian_met_level_two_count = models.IntegerField(
        _('Number of asian students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_hispanic_met_level_two_count = models.IntegerField(
        _('Number of Hispanic students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_pacific_islander_met_level_two_count = models.IntegerField(
        _('Number of Pacific Islander students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_two_or_more_races_met_level_two_count = models.IntegerField(
        _('Number of students of two or more races who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_white_met_level_two_count = models.IntegerField(
        _('Number of white students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_at_risk_met_level_two_count = models.IntegerField(
        _('Number of at risk students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_economically_disadvantaged_met_level_two_count = models.IntegerField(
        _('Number of economically disadvantaged students who met STAAR level 2 phase-in'),
        null=True, blank=True,
        db_column='staar_all_subjects_econ_disadv_met_level_two_count')

    staar_all_subjects_all_students_met_level_two_percent = models.FloatField(
        _('Percent of all students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_african_american_met_level_two_percent = models.FloatField(
        _('Percent of African American students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_american_indian_met_level_two_percent = models.FloatField(
        _('Percent of American Indian students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_asian_met_level_two_percent = models.FloatField(
        _('Percent of asian students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_hispanic_met_level_two_percent = models.FloatField(
        _('Percent of Hispanic students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_pacific_islander_met_level_two_percent = models.FloatField(
        _('Percent of Pacific Islander students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_two_or_more_races_met_level_two_percent = models.FloatField(
        _('Percent of students of two or more races who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_white_met_level_two_percent = models.FloatField(
        _('Percent of white students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_at_risk_met_level_two_percent = models.FloatField(
        _('Percent of at risk students who met STAAR level 2 phase-in'),
        null=True, blank=True)
    staar_all_subjects_economically_disadvantaged_met_level_two_percent = models.FloatField(
        _('Percent of economically disadvantaged students who met STAAR level 2 phase-in'),
        null=True, blank=True,
        db_column='staar_all_subjects_econ_disadv_met_level_two_percent')

    class Meta:
        abstract = True
