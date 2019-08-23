# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class PersonnelBase(models.Model):
    """
    An abstract model representing an administrator attached to an entity.

    Example:

    class Superintendent(PersonnelBase):
        ...

    """
    name = models.CharField(_('Name of personnel'), max_length=254)
    role = models.CharField(_('Role of personnel'), max_length=100)

    email = models.EmailField(_('Email of personnel'))
    phone_number = PhoneNumberField(_('Phone number of personnel'), null=True, blank=True)
    phone_number_extension = models.CharField(
        _('Phone number extension'), max_length=4, blank=True, default='')
    fax_number = PhoneNumberField(_('Fax number of personnel'), null=True, blank=True)
    fax_number_extension = models.CharField(
        _('Fax number extension'), max_length=4, blank=True, default='')

    class Meta:
        abstract = True
