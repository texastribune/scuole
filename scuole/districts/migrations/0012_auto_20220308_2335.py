# Generated by Django 3.1.12 on 2022-03-08 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0011_auto_20220308_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districtstats',
            name='accountability_rating_18_19',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('P', 'Not rated (Paired campus)'), ('DD', 'Not Rated: Declared State of Disaster'), ('', None)], default='', max_length=2, null=True, verbose_name='Accountability rating from 2018-19'),
        ),
        migrations.AlterField(
            model_name='districtstats',
            name='closing_the_gaps_rating_18_19',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('P', 'Not rated (Paired campus)'), ('DD', 'Not Rated: Declared State of Disaster'), ('', None)], default='', max_length=2, null=True, verbose_name='Closing the gaps rating from 2018-19'),
        ),
        migrations.AlterField(
            model_name='districtstats',
            name='school_progress_rating_18_19',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('P', 'Not rated (Paired campus)'), ('DD', 'Not Rated: Declared State of Disaster'), ('', None)], default='', max_length=2, null=True, verbose_name='School progress rating from 2018-19'),
        ),
        migrations.AlterField(
            model_name='districtstats',
            name='student_achievement_rating_18_19',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('P', 'Not rated (Paired campus)'), ('DD', 'Not Rated: Declared State of Disaster'), ('', None)], default='', max_length=2, null=True, verbose_name='Student achievement rating from 2018-19'),
        ),
    ]
