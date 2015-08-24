# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from localflavor.us.models import USStateField

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.counties.models import County
from scuole.districts.models import District
from scuole.stats.models import SchoolYear, StatsBase


@python_2_unicode_compatible
class Campus(models.Model):
    EARLY_EDUCATION = 'EE'
    PRE_KINDERGARTEN = 'PK'
    KINDERGARTEN = 'KG'
    FIRST_GRADE = '01'
    SECOND_GRADE = '02'
    THIRD_GRADE = '03'
    FOURTH_GRADE = '04'
    FIFTH_GRADE = '05'
    SIXTH_GRADE = '06'
    SEVENTH_GRADE = '07'
    EIGHTH_GRADE = '08'
    NINTH_GRADE = '09'
    TENTH_GRADE = '10'
    ELEVENTH_GRADE = '11'
    TWELFTH_GRADE = '12'

    GRADE_CHOICES = (
        (EARLY_EDUCATION, 'Early education'),
        (PRE_KINDERGARTEN, 'Pre-kindergarten'),
        (KINDERGARTEN, 'Kindergarten'),
        (FIRST_GRADE, '1st Grade'),
        (SECOND_GRADE, '2nd Grade'),
        (THIRD_GRADE, '3rd Grade'),
        (FOURTH_GRADE, '4th Grade'),
        (FIFTH_GRADE, '5th Grade'),
        (SIXTH_GRADE, '6th Grade'),
        (SEVENTH_GRADE, '7th Grade'),
        (EIGHTH_GRADE, '8th Grade'),
        (NINTH_GRADE, '9th Grade'),
        (TENTH_GRADE, '10th Grade'),
        (ELEVENTH_GRADE, '11th Grade'),
        (TWELFTH_GRADE, '12th Grade'),
    )

    # CCD - SCHNAM
    name = models.CharField('Campus name', max_length=200)
    slug = models.SlugField(max_length=150)
    # TEA - CAMPUS
    tea_id = models.CharField('TEA campus identifier', max_length=10)
    # CCD - PHONE
    phone = models.CharField('Campus phone number', max_length=10)
    # CCD - LSTREE
    street = models.CharField('Campus street', max_length=100)
    # CCD - LCITY
    city = models.CharField('Campus city', max_length=200)
    # CCD - LSTATE
    state = USStateField('Campus state', max_length=2)
    # CCD - LZIP
    zip_code = models.CharField('Campus ZIP Code', max_length=5)
    # CCD - LZIP4
    zip_code4 = models.CharField('Campus +4 ZIP Code', max_length=4)
    # CCD - ULOCAL
    locale = models.CharField(
        'Campus NCES urban-centric locale identifier', max_length=15)
    # CCD - LATCOD
    latitude = models.FloatField('Campus latitude')
    # CCD - LONCOD
    longitude = models.FloatField('Campus longitude')
    # TEA - GRDSPAN
    low_grade = models.CharField(
        'Lowest grade offered', max_length=2, choices=GRADE_CHOICES)
    high_grade = models.CharField(
        'Highest grade offered', max_length=2, choices=GRADE_CHOICES)

    district = models.ForeignKey(District, related_name='campuses')
    county = models.ForeignKey(County, related_name='campuses')

    class Meta:
        verbose_name_plural = 'campuses'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class CampusStats(StatsBase):
    campus = models.ForeignKey(Campus, related_name='stats')
    year = models.ForeignKey(SchoolYear, related_name='campus_stats')

    class Meta:
        unique_together = ('campus', 'year',)
        verbose_name_plural = 'Campus stats'

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.campus.name)
