# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counties', '0002_auto_20150512_1542'),
        ('districts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Campus name', max_length=200)),
                ('slug', models.SlugField()),
                ('tea_id', models.CharField(help_text='TEA campus identifier', max_length=10)),
                ('phone', models.CharField(help_text='Campus phone number', max_length=10)),
                ('street', models.CharField(help_text='Campus street', max_length=100)),
                ('city', models.CharField(help_text='Campus city', max_length=200)),
                ('state', models.CharField(help_text='Campus state', max_length=5)),
                ('zip_code', models.CharField(help_text='Campus ZIP Code', max_length=5)),
                ('zip_code4', models.CharField(help_text='Campus +4 ZIP Code', max_length=4)),
                ('locale', models.CharField(help_text='Campus NCES urban-centric locale identifier', max_length=15)),
                ('latitude', models.FloatField(help_text='Campus latitude')),
                ('longitude', models.FloatField(help_text='Campus longitude')),
                ('low_grade', models.CharField(help_text='Lowest grade offered', max_length=2, choices=[('EE', 'Early education'), ('PK', 'Pre-kindergarten'), ('KG', 'Kindergarten'), ('01', '1st Grade'), ('02', '2nd Grade'), ('03', '3rd Grade'), ('04', '4th Grade'), ('05', '5th Grade'), ('06', '6th Grade'), ('07', '7th Grade'), ('08', '8th Grade'), ('09', '9th Grade'), ('10', '10th Grade'), ('11', '11th Grade'), ('12', '12th Grade')])),
                ('high_grade', models.CharField(help_text='Highest grade offered', max_length=2, choices=[('EE', 'Early education'), ('PK', 'Pre-kindergarten'), ('KG', 'Kindergarten'), ('01', '1st Grade'), ('02', '2nd Grade'), ('03', '3rd Grade'), ('04', '4th Grade'), ('05', '5th Grade'), ('06', '6th Grade'), ('07', '7th Grade'), ('08', '8th Grade'), ('09', '9th Grade'), ('10', '10th Grade'), ('11', '11th Grade'), ('12', '12th Grade')])),
                ('county', models.ForeignKey(related_name='campuses', to='counties.County')),
                ('district', models.ForeignKey(related_name='campuses', to='districts.District')),
            ],
        ),
    ]
