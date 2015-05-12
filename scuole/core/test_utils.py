# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.test import TestCase

from . import utils


class CoreUtilsTest(TestCase):

    def test_string_replace(self):
        converted = utils.string_replace('Beaumont Isd', {
            'Isd': 'ISD'
        })

        self.assertEquals(converted, 'Beaumont ISD')

    def test_cap_after_dash(self):
        converted = utils.cap_after_dash('Uplift Education-summit')

        self.assertEquals(converted, 'Uplift Education-Summit')

    def test_cap_after_parenthesis(self):
        s = 'Richard Milburn Academy (ector County)'
        converted = utils.cap_after_parenthesis(s)

        self.assertEquals(converted, 'Richard Milburn Academy (Ector County)')

    def test_acad_to_academy(self):
        converted = utils.acad_to_academy('Harmony Science Acad (Waco)')

        self.assertEquals(converted, 'Harmony Science Academy (Waco)')

    def test_acad_to_academy_not_double_academy(self):
        converted = utils.acad_to_academy('Midland Academy Charter School')

        self.assertNotEquals(converted, 'Midland Academyemy Charter School')

    def test_acad_to_academy_plural_academies(self):
        converted = utils.acad_to_academy(
            'Texas College Preparatory Academies')

        self.assertNotEquals(
            converted, 'Texas College Preparatory Academyemies')

    def test_acad_to_academy_spanish(self):
        converted = utils.acad_to_academy(
            'La Academia de Estrellas')

        self.assertNotEquals(
            converted, 'La Academyemia de Estrellas')
