from django.db import models

# Create your models here.
class State(models.Model):
    # This data is current from 2012-2013 CCD unlike
    # School and District which are both from 2013-2014.
    name = models.CharField(help_text="State name", max_length=50)
    phone = models.CharField(help_text="State phone number", max_length=10)
    city = models.CharField(help_text="State city", max_length=200)
    zip = models.CharField(help_text="State zip", max_length=5)
    zip4 = models.CharField(help_text="State +4 zip", max_length=4)
    latitude = models.FloatField(help_text="State latitude")
    longitude = models.FloatField(help_text="State longitude")
