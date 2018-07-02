# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import string

from localflavor.us.models import (
    PhoneNumberField, USStateField, USZipCodeField)

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.core.models import PersonnelBase
from scuole.counties.models import County
from scuole.districts.models import District
from scuole.stats.models import ReferenceBase, SchoolYear, StatsBase
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
        (FIRST_GRADE, _('1st grade')),
        (SECOND_GRADE, _('2nd grade')),
        (THIRD_GRADE, _('3rd grade')),
        (FOURTH_GRADE, _('4th grade')),
        (FIFTH_GRADE, _('5th grade')),
        (SIXTH_GRADE, _('6th grade')),
        (SEVENTH_GRADE, _('7th grade')),
        (EIGHTH_GRADE, _('8th grade')),
        (NINTH_GRADE, _('9th grade')),
        (TENTH_GRADE, _('10th grade')),
        (ELEVENTH_GRADE, _('11th grade')),
        (TWELFTH_GRADE, _('12th grade')),
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

    name = models.CharField(_('Campus name'), max_length=200)
    slug = models.SlugField(max_length=150)
    # TEA - CAMPUS
    tea_id = models.CharField(_('TEA campus identifier'), max_length=10)
    phone_number = PhoneNumberField(
        _('Campus phone number'), max_length=20, null=True)
    phone_number_extension = models.CharField(
        _('Phone number extension'), max_length=4, blank=True, default='')
    website = models.URLField(
        _('Campus website'), blank=True, default='')
    charter = models.BooleanField(_('Charter status'), default=False)
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

    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        related_name='campuses',
    )
    county = models.ForeignKey(
        County,
        on_delete=models.CASCADE,
        related_name='campuses',
    )

    class Meta:
        ordering = ['name']
        verbose_name_plural = _('campuses')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('districts:campus', kwargs={
            'slug': self.slug,
            'district_slug': self.district.slug,
        })

    @property
    def city_display(self):
        if self.city:
            return string.capwords(self.city)
        else:
            return ''

    @property
    def location(self):
        if self.city and self.state:
            return '{city}, {state}'.format(
                city=string.capwords(self.city),
                state=self.state)
        else:
            return ''

    @property
    def location_full(self):
        if self.city and self.state:
            return '{city}, {state}'.format(
                city=string.capwords(self.city),
                state=self.get_state_display())
        else:
            return ''

    @property
    def is_secondary_school(self):
        return (self.school_type == 'S' or self.school_type == 'B')


@python_2_unicode_compatible
class CampusStats(StatsBase, ReferenceBase):
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        related_name='stats',
    )
    year = models.ForeignKey(
        SchoolYear,
        on_delete=models.CASCADE,
        related_name='campus_stats',
    )

    class Meta:
        unique_together = ('campus', 'year',)
        verbose_name_plural = _('Campus stats')

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.campus.name)


@python_2_unicode_compatible
class Principal(PersonnelBase):
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        related_name='principals',
    )

    def __str__(self):
        return '{} at {}'.format(self.name, self.campus.name)
