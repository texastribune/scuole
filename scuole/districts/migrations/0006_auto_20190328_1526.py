# Generated by Django 2.1.7 on 2019-03-28 15:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0005_auto_20170216_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtstats',
            name='closing_the_gaps_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated due to data integrity issue'), ('T', 'Not rated due to annexation'), ('H', 'Not rated due to Harvey provision')], default='', max_length=1, verbose_name='Closing the gaps rating'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='school_progress_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated due to data integrity issue'), ('T', 'Not rated due to annexation'), ('H', 'Not rated due to Harvey provision')], default='', max_length=1, verbose_name='School progress rating'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='student_achievement_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated due to data integrity issue'), ('T', 'Not rated due to annexation'), ('H', 'Not rated due to Harvey provision')], default='', max_length=1, verbose_name='Student achievement rating'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='uses_legacy_ratings',
            field=models.BooleanField(default=True, help_text='This Stats model uses the old accountability system'),
        ),
        migrations.AlterField(
            model_name='districtstats',
            name='accountability_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated due to data integrity issue'), ('T', 'Not rated due to annexation'), ('H', 'Not rated due to Harvey provision')], default='', max_length=1, verbose_name='Accountability rating'),
        ),
        migrations.AlterField(
            model_name='superintendent',
            name='fax_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Fax number of personnel'),
        ),
        migrations.AlterField(
            model_name='superintendent',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number of personnel'),
        ),
    ]
