# Generated by Django 2.2.4 on 2019-08-08 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0008_auto_20190328_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campusstats',
            name='accountability_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('', None)], default='', max_length=1, verbose_name='Accountability rating'),
        ),
        migrations.AlterField(
            model_name='campusstats',
            name='closing_the_gaps_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('', None)], default='', max_length=1, verbose_name='Closing the gaps rating'),
        ),
        migrations.AlterField(
            model_name='campusstats',
            name='school_progress_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('', None)], default='', max_length=1, verbose_name='School progress rating'),
        ),
        migrations.AlterField(
            model_name='campusstats',
            name='student_achievement_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('T', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated (data integrity issue)'), ('T', 'Not rated (Annexed)'), ('H', 'Not rated (Harvey provision)'), ('', None)], default='', max_length=1, verbose_name='Student achievement rating'),
        ),
    ]
