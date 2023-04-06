# Generated by Django 3.1.12 on 2023-03-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0015_auto_20230324_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districtstats',
            name='accountability_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('P', 'Not rated (Paired campus)'), ('DD', 'Not Rated: Declared State of Disaster'), ('R', 'Not Rated: Data Under Review'), ('SB', 'Not Rated: Senate Bill 1365'), ('SB', 'Not Rated: SB 1365'), ('', None)], default='', max_length=2, verbose_name='Accountability rating from the latest year'),
        ),
        migrations.AlterField(
            model_name='districtstats',
            name='accountability_rating_18_19',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('P', 'Not rated (Paired campus)'), ('DD', 'Not Rated: Declared State of Disaster'), ('R', 'Not Rated: Data Under Review'), ('SB', 'Not Rated: Senate Bill 1365'), ('SB', 'Not Rated: SB 1365'), ('', None)], default='', max_length=2, null=True, verbose_name='Accountability rating from 2018-19'),
        ),
        migrations.AlterField(
            model_name='districtstats',
            name='closing_the_gaps_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('P', 'Not rated (Paired campus)'), ('DD', 'Not Rated: Declared State of Disaster'), ('R', 'Not Rated: Data Under Review'), ('SB', 'Not Rated: Senate Bill 1365'), ('SB', 'Not Rated: SB 1365'), ('', None)], default='', max_length=2, verbose_name='Closing the gaps rating from the latest year'),
        ),
        migrations.AlterField(
            model_name='districtstats',
            name='closing_the_gaps_rating_18_19',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('P', 'Not rated (Paired campus)'), ('DD', 'Not Rated: Declared State of Disaster'), ('R', 'Not Rated: Data Under Review'), ('SB', 'Not Rated: Senate Bill 1365'), ('SB', 'Not Rated: SB 1365'), ('', None)], default='', max_length=2, null=True, verbose_name='Closing the gaps rating from 2018-19'),
        ),
        migrations.AlterField(
            model_name='districtstats',
            name='school_progress_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('P', 'Not rated (Paired campus)'), ('DD', 'Not Rated: Declared State of Disaster'), ('R', 'Not Rated: Data Under Review'), ('SB', 'Not Rated: Senate Bill 1365'), ('SB', 'Not Rated: SB 1365'), ('', None)], default='', max_length=2, verbose_name='School progress rating from the latest year'),
        ),
        migrations.AlterField(
            model_name='districtstats',
            name='school_progress_rating_18_19',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('P', 'Not rated (Paired campus)'), ('DD', 'Not Rated: Declared State of Disaster'), ('R', 'Not Rated: Data Under Review'), ('SB', 'Not Rated: Senate Bill 1365'), ('SB', 'Not Rated: SB 1365'), ('', None)], default='', max_length=2, null=True, verbose_name='School progress rating from 2018-19'),
        ),
        migrations.AlterField(
            model_name='districtstats',
            name='student_achievement_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('P', 'Not rated (Paired campus)'), ('DD', 'Not Rated: Declared State of Disaster'), ('R', 'Not Rated: Data Under Review'), ('SB', 'Not Rated: Senate Bill 1365'), ('SB', 'Not Rated: SB 1365'), ('', None)], default='', max_length=2, verbose_name='Student achievement rating from the latest year'),
        ),
        migrations.AlterField(
            model_name='districtstats',
            name='student_achievement_rating_18_19',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('P', 'Not rated (Paired campus)'), ('DD', 'Not Rated: Declared State of Disaster'), ('R', 'Not Rated: Data Under Review'), ('SB', 'Not Rated: Senate Bill 1365'), ('SB', 'Not Rated: SB 1365'), ('', None)], default='', max_length=2, null=True, verbose_name='Student achievement rating from 2018-19'),
        ),
    ]
