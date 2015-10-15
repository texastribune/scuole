# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import string

from localflavor.us.models import USStateField, USZipCodeField, PhoneNumberField

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.core.models import PersonnelBase
from scuole.counties.models import County
from scuole.districts.models import District
from scuole.stats.models import SchoolYear, StatsBase
from django.utils.translation import ugettext_lazy as _


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
        (EARLY_EDUCATION, _('Early education')),
        (PRE_KINDERGARTEN, _('Pre-kindergarten')),
        (KINDERGARTEN, _('Kindergarten')),
        (FIRST_GRADE, _('1st Grade')),
        (SECOND_GRADE, _('2nd Grade')),
        (THIRD_GRADE, _('3rd Grade')),
        (FOURTH_GRADE, _('4th Grade')),
        (FIFTH_GRADE, _('5th Grade')),
        (SIXTH_GRADE, _('6th Grade')),
        (SEVENTH_GRADE, _('7th Grade')),
        (EIGHTH_GRADE, _('8th Grade')),
        (NINTH_GRADE, _('9th Grade')),
        (TENTH_GRADE, _('10th Grade')),
        (ELEVENTH_GRADE, _('11th Grade')),
        (TWELFTH_GRADE, _('12th Grade')),
    )

    ELEMENTARY_SCHOOL = 'E'
    MIDDLE_SCHOOL = 'M'
    HIGH_SCHOOL = 'S'
    ELEMENTARY_SECONDARY_SCHOOL = 'B'

    SCHOOL_TYPE_CHOICES = (
        (ELEMENTARY_SCHOOL, _('Elementary school')),
        (MIDDLE_SCHOOL, _('Middle school or junior high school')),
        (HIGH_SCHOOL, _('High school')),
        (ELEMENTARY_SECONDARY_SCHOOL, _('Elementary/secondary school')),
    )

    MET_STANDARD = 'M'
    MET_ALTERNATIVE_STANDARD = 'A'
    IMPROVEMENT_REQUIRED = 'I'
    NOT_RATED = 'X'
    NOT_RATED = 'Z'
    NOT_RATED_DUE_TO_DATA_INTEGRITY_ISSUE = 'Q'

    RATING_CHOICES = (
        (MET_STANDARD, _('Met standard')),
        (MET_ALTERNATIVE_STANDARD, _('Met alternative standard')),
        (IMPROVEMENT_REQUIRED, _('Improvement required')),
        (NOT_RATED, _('Not rated')),
        (NOT_RATED_DUE_TO_DATA_INTEGRITY_ISSUE,
            _('Not rated due to data integrity issue')),
    )

    name = models.CharField(_('Campus name'), max_length=200)
    slug = models.SlugField(max_length=150)
    # TEA - CAMPUS
    tea_id = models.CharField(_('TEA campus identifier'), max_length=10)
    phone_number = PhoneNumberField(
        _('Campus phone number'), max_length=20, null=True)
    phone_number_extension = models.CharField(
        _('Phone number extension'), max_length=4, blank=True, default='')
    street = models.CharField(_('Campus street'), max_length=100, null=True)
    city = models.CharField(_('Campus city'), max_length=200, null=True)
    state = USStateField(_('Campus state'), max_length=2, null=True)
    zip_code = USZipCodeField(_('Campus ZIP Code'), null=True)
    locale = models.CharField(
        _('Campus NCES urban-centric locale identifier'), max_length=15)
    coordinates = models.PointField(null=True)
    # TEA - GRDSPAN
    low_grade = models.CharField(
        _('Lowest grade offered'), max_length=2, choices=GRADE_CHOICES)
    high_grade = models.CharField(
        _('Highest grade offered'), max_length=2, choices=GRADE_CHOICES)
    school_type = models.CharField(
        _('School type'), max_length=1, choices=SCHOOL_TYPE_CHOICES)
    accountability_rating = models.CharField(
        _('Accountability rating'), max_length=1, choices=RATING_CHOICES)

    district = models.ForeignKey(District, related_name='campuses')
    county = models.ForeignKey(County, related_name='campuses')
    objects = models.GeoManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = _('campuses')

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
        verbose_name_plural = _('Campus stats')

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.campus.name)


@python_2_unicode_compatible
class Principal(PersonnelBase):
    campus = models.ForeignKey(Campus, related_name='principals')

    def __str__(self):
        return '{} at {}'.format(self.name, self.campus.name)
