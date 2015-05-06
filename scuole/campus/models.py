from django.db import models
from django.utils.text import slugify


class Campus(models.Model):
    slug = models.SlugField()
    # CCD fields
    name = models.CharField(help_text="Campus name", max_length=200)
    phone = models.CharField(
        help_text="Campus phone number", max_length=10)
    city = models.CharField(
        help_text="Campus city", max_length=200)
    zip = models.CharField(
        help_text="Campus zip", max_length=5)
    zip4 = models.CharField(
        help_text="Campus +4 zip", max_length=4)
    status = models.CharField(
        help_text="Campus NCES status code", max_length=1)
    locale = models.CharField(
        help_text="Campus NCES urban-centric locale code", max_length=2)
    latitude = models.FloatField(help_text="Campus latitude")
    longitude = models.FloatField(help_text="Campus longitude")
    # TAPR fields
    rating = models.CharField(
        help_text="Campus rating", max_length=1)
    campus_id = models.CharField(
        help_text="Campus ID", max_length=10)
    charter = models.CharField(
        help_text="Chartered campus", max_length=1)
    county = models.CharField(
        help_text="County campus is located", max_length=100)
    district = models.CharField(
        help_text="District number campus is located", max_length=100)
    grade_span = models.CharField(
        help_text="Campus span of grade levels based on enrollment",
        max_length=6)
    level = models.CharField(
        help_text="Campus type: Elementary, Middle, Senior or Both",
        max_length=1)
    # student breakdown
    all_students = models.IntegerField(
        help_text="Campus total student enrollment")
    african_american = models.FloatField(
        help_text="Percent of African American students enrolled at campus")
    hispanic = models.FloatField(
        help_text="Percent of Hispanic students enrolled at campus")
    asian = models.FloatField(
        help_text="Percent of Asian students enrolled at campus")

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)[:50]

        super(Campus, self).save(*args, **kwargs)
