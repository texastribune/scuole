from django.db import models

# Create your models here.
class County(models.Model):
    district = model.CharField(
        help_text="Districts located withinin county", max_length=200)
    campus = model.CharField(
        help_text="Campuses located within county", max_length=200)
    region = model.CharField(
        help_text="Region located within county", max_length=100)
