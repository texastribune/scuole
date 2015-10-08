# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from localflavor.us.models import PhoneNumberField

from django.db import models


class PersonnelBase(models.Model):
    """
    An abstract model representing an administrator attached to an entity.

    Example:

    class Superintendent(PersonnelBase):
        ...

    """
    name = models.CharField('Name of personnel', max_length=254)
    role = models.CharField('Role of personnel', max_length=100)

    email = models.EmailField('Email of personnel')
    phone_number = PhoneNumberField('Phone number of personnel')
    phone_number_extension = models.IntegerField(
        'Phone number extension', null=True, blank=True)
    fax_number = PhoneNumberField('Fax number of personnel')

    class Meta:
        abstract = True
