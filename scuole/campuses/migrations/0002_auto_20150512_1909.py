# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='locale',
            field=models.CharField(default=('22',), help_text='Campus NCES urban-centric locale code', max_length=2, choices=[(('11',), 'City, Large Territory inside an urbanized area and inside a principal city with population of 250,000 or more.'), (('12',), 'City, Mid-size Territory inside an urbanized area and inside a principal city with a population less than 250,000 and greater than or equal to 100,000.'), (('13',), 'City, Small Territory inside an urbanized area and inside a principal city with a population less than 100,000.'), (('21',), 'Suburb, Large Territory outside a principal city and inside an urbanized area with population of 250,000 or more.'), (('22',), 'Suburb, Mid-size Territory outside a principal city and inside an urbanized area with a population less than 250,000 and greater than or equal to 100,000.'), (('23',), 'Suburb, Small Territory outside a principal city and inside an urbanized area with a population less than 100,000.'), (('31',), 'Town, Fringe Territory inside an urban cluster that is less than or equal to 10 miles from an urbanized area.'), (('32',), 'Town, Distant Territory inside an urban cluster that is more than 10 miles and less than or equal to 35 miles from an urbanized area.'), (('33',), 'Town, Remote Territory inside an urban cluster that is more than 35 miles from an urbanized area.'), (('41',), 'Rural, Fringe Census-defined rural territory that is less than or equal to 5 miles from an urbanized area, as well as rural territory that is less than or equal to 2.5 miles from an urban cluster.'), (('42',), 'Rural, Distant Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an urbanized area, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an urban cluster.'), (('43',), 'Rural, Remote Census-defined rural territory that is more than 25 miles from an urbanized area and is also more than 10 miles from an urban cluster.')]),
        ),
        migrations.AlterField(
            model_name='campus',
            name='status',
            field=models.CharField(default=('1',), help_text='Campus NCES status code', max_length=1, choices=[(('1',), 'School was operational at the time of the last report and is currently operational.'), (('2',), 'School has closed since the time of the last report.'), (('3',), 'School has been opened since the time of the last report.'), (('4',), 'School was in existence, but not reported in a previous year\u2019s CCD school universe survey, and is now being added.'), (('5',), 'School was listed in previous year\u2019s CCD school universe as being affiliated with a different education agency.'), (('6',), 'School is temporarily closed and may reopen within 3 years.'), (('7',), 'School is scheduled to be operational within 2 years.'), (('8',), 'School was closed on a previous year\u2019s file but has reopened.')]),
        ),
    ]
