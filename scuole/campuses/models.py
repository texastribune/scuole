# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.districts.models import District


@python_2_unicode_compatible
class Campus(models.Model):
    # CCD campus status choices
    OPERATIONAL = '1',
    CLOSED = '2',
    OPENED = '3',
    ADDED_TO_SURVEY = '4',
    NEW_AFFILIATION = '5',
    TEMPORARILY_CLOSED = '6',
    SCHEDULED_OPENING = '7',
    REOPENED = '8',

    STATUS_CHOICES = (
        (OPERATIONAL, 
            'School was operational at the time of the last report and is currently operational.'),
        (CLOSED,
            'School has closed since the time of the last report.'),
        (OPENED,
        	'School has been opened since the time of the last report.'),
        (ADDED_TO_SURVEY,
        	'School was in existence, but not reported in a previous year’s CCD school universe survey, and is now being added.'),
        (NEW_AFFILIATION,
        	'School was listed in previous year’s CCD school universe as being affiliated with a different education agency.'),
        (TEMPORARILY_CLOSED,
        	'School is temporarily closed and may reopen within 3 years.'),
        (SCHEDULED_OPENING,
        	'School is scheduled to be operational within 2 years.'),
        (REOPENED,
        	'School was closed on a previous year’s file but has reopened.'),
    )
    # CCD campus locale choices
    LARGE_CITY = '11',
    MID_SIZE_CITY = '12',
    SMALL_CITY = '13',
    LARGE_SUBURB = '21',
    MID_SIZE_SUBURB = '22'.
    SMALL_SUBURB = '23',
    FRINGE_TOWN = '31',
    DISTANT_TOWN = '32',
    REMOTE_TOWN = '33',
    FRINGE_RURAL = '41',
    DISTANT_RURAL = '42',
    REMOTE_RURAL = '43',

    LOCALE_CHOICES = (
    	(LARGE_CITY,
    		'City, Large Territory inside an urbanized area and inside a principal city with population of 250,000 or more.'),
    	(MID_SIZE_CITY,
    		'City, Mid-size Territory inside an urbanized area and inside a principal city with a population less than 250,000 and greater than or equal to 100,000.'),
    	(SMALL_CITY,
    		'City, Small Territory inside an urbanized area and inside a principal city with a population less than 100,000.'),
    	(LARGE_SUBURB,
			'Suburb, Large Territory outside a principal city and inside an urbanized area with population of 250,000 or more.'),
    	(MID_SIZE_SUBURB,
    		'Suburb, Mid-size Territory outside a principal city and inside an urbanized area with a population less than 250,000 and greater than or equal to 100,000.'),
    	(SMALL_SUBURB,
    		'Suburb, Small Territory outside a principal city and inside an urbanized area with a population less than 100,000.'),
    	(FRINGE_TOWN,
    		'Town, Fringe Territory inside an urban cluster that is less than or equal to 10 miles from an urbanized area.'),
    	(DISTANT_TOWN,
    		'Town, Distant Territory inside an urban cluster that is more than 10 miles and less than or equal to 35 miles from an urbanized area.'),
    	(REMOTE_TOWN,
    		'Town, Remote Territory inside an urban cluster that is more than 35 miles from an urbanized area.'),
    	(FRINGE_RURAL,
    		'Rural, Fringe Census-defined rural territory that is less than or equal to 5 miles from an urbanized area, as well as rural territory that is less than or equal to 2.5 miles from an urban cluster.'),
    	(DISTANT_RURAL,
    		'Rural, Distant Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an urbanized area, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an urban cluster.'),
    	(REMOTE_RURAL,
    		'Rural, Remote Census-defined rural territory that is more than 25 miles from an urbanized area and is also more than 10 miles from an urban cluster.')
    )
    # CCD - SCHNAM
    name = models.CharField(
        help_text="Campus name", max_length=200)
    slug = models.SlugField()
    # TEA - CAMPUS
    tea_id = models.CharField(
        help_text="TEA campus identifier",
        max_length=10)
    # CCD - PHONE
    phone = models.CharField(
        help_text="Campus phone number",
        max_length=10)
    # CCD - LSTREE
    street = models.CharField(
        help_text="Campus street",
        max_length=100)
    # CCD - LCITY
    city = models.CharField(
        help_text="Campus city",
        max_length=200)
    # CCD - LSTATE
    state = models.CharField(
        help_text="Campus state",
        max_length=5)
    # CCD - LZIP
    zip_code = models.CharField(
        help_text="Campus ZIP Code",
        max_length=5)
    # CCD - LZIP4
    zip_code4 = models.CharField(
        help_text="Campus +4 ZIP Code",
        max_length=4)
    # CCD - STATUS
    status = models.CharField(
        help_text="Campus NCES status code",
        max_length=1,
        choices=STATUS_CHOICES,
        default=OPERATIONAL)
    # CCD - ULOCAL
    locale = models.CharField(
        help_text="Campus NCES urban-centric locale code",
        max_length=2,
        choices=LOCALE_CHOICES,
        default=MID_SIZE_SUBURB)
    # CCD - LATCOD
    latitude = models.FloatField(help_text="Campus latitude")
    # CCD - LONCOD
    longitude = models.FloatField(help_text="Campus longitude")
    district = models.ForeignKey(District, related_name="campuses")

    def __str__(self):
        return self.name
