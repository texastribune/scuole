# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import string

from localflavor.us.models import USStateField, USZipCodeField

from django.contrib.gis.db import models
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

    ELEMENTARY_SCHOOL = 'E'
    MIDDLE_SCHOOL = 'M'
    HIGH_SCHOOL = 'S'
    ELEMENTARY_SECONDARY_SCHOOL = 'B'

    SCHOOL_TYPE_CHOICES = (
        (ELEMENTARY_SCHOOL, 'Elementary school'),
        (MIDDLE_SCHOOL, 'Middle school or junior high school'),
        (HIGH_SCHOOL, 'High school'),
        (ELEMENTARY_SECONDARY_SCHOOL, 'Elementary/secondary school'),
    )

    MET_STANDARD = 'M'
    MET_ALTERNATIVE_STANDARD = 'A'
    IMPROVEMENT_REQUIRED = 'I'
    NOT_RATED = 'X'
    NOT_RATED = 'Z'
    NOT_RATED_DUE_TO_DATA_INTEGRITY_ISSUE = 'Q'

    RATING_CHOICES = (
        (MET_STANDARD, 'Met standard'),
        (MET_ALTERNATIVE_STANDARD, 'Met alternative standard'),
        (IMPROVEMENT_REQUIRED, 'Improvement required'),
        (NOT_RATED, 'Not rated'),
        (NOT_RATED_DUE_TO_DATA_INTEGRITY_ISSUE,
            'Not rated due to data integrity issue'),
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
    # CCD - LZIP-LZIP4
    zip_code = USZipCodeField('Campus ZIP Code')
    # CCD - ULOCAL
    locale = models.CharField(
        'Campus NCES urban-centric locale identifier', max_length=15)
    # CCD - LATCOD
    coordinates = models.PointField(null=True)
    # TEA - GRDSPAN
    low_grade = models.CharField(
        'Lowest grade offered', max_length=2, choices=GRADE_CHOICES)
    high_grade = models.CharField(
        'Highest grade offered', max_length=2, choices=GRADE_CHOICES)
    school_type = models.CharField(
        'School type', max_length=1, choices=SCHOOL_TYPE_CHOICES)
    accountability_rating = models.CharField(
        'Accountability rating', max_length=3, choices=RATING_CHOICES
    )

    district = models.ForeignKey(District, related_name='campuses')
    county = models.ForeignKey(County, related_name='campuses')
    objects = models.GeoManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'campuses'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('districts:campus', kwargs={
            'slug': self.slug,
            'district_id': self.district.pk,
            'district_slug': self.district.slug,
        })

    @property
    def location(self):
        return '{city}, {state}'.format(
            city=string.capwords(self.city),
            state=self.state)


@python_2_unicode_compatible
class CampusStats(StatsBase):
    campus = models.ForeignKey(Campus, related_name='stats')
    year = models.ForeignKey(SchoolYear, related_name='campus_stats')

    class Meta:
        unique_together = ('campus', 'year',)
        verbose_name_plural = 'Campus stats'

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.campus.name)
