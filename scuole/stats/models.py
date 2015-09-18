# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class SchoolYear(models.Model):
    name = models.CharField(max_length=9)

    def __str__(self):
        return self.name


class StatsBase(models.Model):
    """
    An abstract model representing stats commonly tracked across all entities
    in TEA data. Meant to be the base used by other apps for establishing
    their stats models.

    Example:

    class CampusStats(StatsBase):
        ...

    """

    # Student counts
    all_students_count = models.IntegerField(
        'Number of students', null=True, blank=True)
    african_american_count = models.IntegerField(
        'Number of African American students', null=True, blank=True)
    american_indian_count = models.FloatField(
        'Number of American Indian students', null=True, blank=True)
    asian_count = models.IntegerField(
        'Number of Asian students', null=True, blank=True)
    hispanic_count = models.IntegerField(
        'Number of Hispanic students', null=True, blank=True)
    pacific_islander_count = models.IntegerField(
        'Number of Pacific Islander students', null=True, blank=True)
    two_or_more_races_count = models.IntegerField(
        'Number of Two or More Races students', null=True, blank=True)
    white_count = models.IntegerField(
        'Number of White students', null=True, blank=True)
    early_childhood_education_count = models.IntegerField(
        'Number of early childhood education students', null=True, blank=True)
    prek_count = models.IntegerField(
        'Number of pre-k students', null=True, blank=True)
    kindergarten_count = models.IntegerField(
        'Number of kindergarten students', null=True, blank=True)
    first_count = models.IntegerField(
        'Number of first grade students', null=True, blank=True)
    second_count = models.IntegerField(
        'Number of second grade students', null=True, blank=True)
    third_count = models.IntegerField(
        'Number of third grade students', null=True, blank=True)
    fourth_count = models.IntegerField(
        'Number of fourth grade students', null=True, blank=True)
    fifth_count = models.IntegerField(
        'Number of fifth grade students', null=True, blank=True)
    sixth_count = models.IntegerField(
        'Number of sixth grade students', null=True, blank=True)
    seventh_count = models.IntegerField(
        'Number of seventh grade students', null=True, blank=True)
    eigth_count = models.IntegerField(
        'Number of eigth grade students', null=True, blank=True)
    ninth_count = models.IntegerField(
        'Number of ninth grade students', null=True, blank=True)
    tenth_count = models.IntegerField(
        'Number of tenth grade students', null=True, blank=True)
    eleventh_count = models.IntegerField(
        'Number of eleventh grade students', null=True, blank=True)
    twelfth_count = models.IntegerField(
        'Number of twelfth grade students', null=True, blank=True)
    at_risk_count = models.IntegerField(
        'Number of at risk students', null=True, blank=True)

    # Student percents
    african_american_percent = models.FloatField(
        'Percent of African American students', null=True, blank=True)
    american_indian_percent = models.FloatField(
        'Percent of American Indian students', null=True, blank=True)
    asian_percent = models.FloatField(
        'Percent of Asian students', null=True, blank=True)
    hispanic_percent = models.FloatField(
        'Percent of Hispanic students', null=True, blank=True)
    pacific_islander_percent = models.FloatField(
        'Percent of Pacific Islander students', null=True, blank=True)
    two_or_more_races_percent = models.FloatField(
        'Percent of Two or More Races students', null=True, blank=True)
    white_percent = models.FloatField(
        'Percent of White students', null=True, blank=True)
    early_childhood_education_percent = models.FloatField(
        'Percent of early childhood education students', null=True, blank=True)
    prek_percent = models.FloatField(
        'Percent of pre-k students', null=True, blank=True)
    kindergarten_percent = models.FloatField(
        'Percent of kindergarten students', null=True, blank=True)
    first_percent = models.FloatField(
        'Percent of first grade students', null=True, blank=True)
    second_percent = models.FloatField(
        'Percent of second grade students', null=True, blank=True)
    third_percent = models.FloatField(
        'Percent of third grade students', null=True, blank=True)
    fourth_percent = models.FloatField(
        'Percent of fourth grade students', null=True, blank=True)
    fifth_percent = models.FloatField(
        'Percent of fifth grade students', null=True, blank=True)
    sixth_percent = models.FloatField(
        'Percent of sixth grade students', null=True, blank=True)
    seventh_percent = models.FloatField(
        'Percent of seventh grade students', null=True, blank=True)
    eighth_percent = models.FloatField(
        'Percent of eighth grade students', null=True, blank=True)
    ninth_percent = models.FloatField(
        'Percent of ninth grade students', null=True, blank=True)
    tenth_percent = models.FloatField(
        'Percent of tenth grade students', null=True, blank=True)
    eleventh_percent = models.FloatField(
        'Percent of eleventh grade students', null=True)
    twelfth_percent = models.FloatField(
        'Percent of twelfth grade students', null=True, blank=True)
    at_risk_percent = models.FloatField(
        'Percent of at risk students', null=True, blank=True)

    # college ready counts
    college_ready_graduates_english_all_students_count = models.IntegerField(
        'Number of college ready students in English',
        null=True, blank=True)
    college_ready_graduates_english_african_american_count = models.IntegerField(
        'Number of college ready African American graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_american_indian_count = models.IntegerField(
        'Number of college ready American Indian graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_asian_count = models.IntegerField(
        'Number of college ready Asian graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_hispanic_count = models.IntegerField(
        'Number of college ready Hispanic graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_native_american_count = models.IntegerField(
        'Number of college ready Native American graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_pacific_islander_count = models.IntegerField(
        'Number of college ready Pacific Islander graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_two_or_more_count = models.IntegerField(
        'Number of college ready graduates of two or more races in English',
        null=True, blank=True)
    college_ready_graduates_english_white_count = models.IntegerField(
        'Number of college ready white graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_econ_disadv_count = models.IntegerField(
        'Number of college ready economically disadvantaged graduates in English',
        null=True, blank=True)

    college_ready_graduates_math_all_students_count = models.IntegerField(
        'Number of college ready students in math',
        null=True, blank=True)
    college_ready_graduates_math_african_american_count = models.IntegerField(
        'Number of college ready African American graduates in math',
        null=True, blank=True)
    college_ready_graduates_math_american_indian_count = models.IntegerField(
        'Number of college ready American Indian graduages in math',
        null=True, blank=True)
    college_ready_graduates_math_asian_count = models.IntegerField(
        'Number of college ready Asian graduates in math',
        null=True, blank=True)
    college_ready_graduates_math_hispanic_count = models.IntegerField(
        'Number of college ready Hispanic graduates in math',
        null=True, blank=True)
    college_ready_graduates_math_native_american_count = models.IntegerField(
        'Number of college ready Native American graduates in math',
        null=True, blank=True)
    college_ready_graduates_math_pacific_islander_count = models.InteferField(
        'Number of college ready Pacific Islander graduates in math',
        null=True, blank=True)
    college_ready_graduates_math_two_or_more_races_count = models.IntegerField(
        'Number of college ready graduages of two or more races in math',
        null=True, blank=True)
    college_ready_graduates_math_white_count = models.IntegerField(
        'Number of college ready white graduates in math',
        null=True, blank=True)
    college_ready_graduates_math_econ_disadv_count = models.IntegerField(
        'Number of college ready economically disadvantaged graduates in math',
        null=True, blank=True)

    college_ready_graduates_both_all_students_count = models.IntegerField(
        'Number of college ready graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_african_american_count = models.IntegerField(
        'Number of college ready african american graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_american_indian_count = models.IntegerField(
        'Number of college ready American Indian graduates in borh subjects',
        null=True, blank=True)
    college_ready_graduates_both_asian_count = models.IntegerField(
        'Number of college ready Asian graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_hispanic_count = models.IntegerField(
        'Number of college ready Hispanic graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_native_american_count = models.IntegerField(
        'Number of college ready Native American graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_pacific_islander_count = models.IntegerField(
        'Number of college ready Pacific Islander graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_two_or_more_races_count = models.IntegerField(
        'Number of college ready graduates of two or more races in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_white_count = models.IntegerField(
        'Number of college ready white graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_econ_disadv_count = models.IntegerField(
        'Number of college ready economically disadvantaged graduates in both subjects',
        null=True, blank=True)

    # college ready percents
    college_ready_graduates_english_all_students_percent = models.FloatField(
        'Percent of college ready graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_african_american_percent = models.FloatField(
        'Percent of college ready African American graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_american_indian_percent = models.FloatField(
        'Percent of college ready American Indian graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_asian_percent = models.FloatField(
        'Percent of college ready Asian graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_hispanic_percent = models.FloatField(
        'Percent of college ready Hispanic graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_native_american_percent = models.FloatField(
        'Percent of college ready Native American graduates in english',
        null=True, blank=True)
    college_ready_graduates_english_pacific_islander_percent = models.FloatField(
        'Percent of college ready Pacific Islander graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_two_or_more_percent = models.FloatField(
        'Percent of college ready graduates of two or more races in English',
        null=True, blank=True)
    college_ready_graduates_english_white_percent = models.FloatField(
        'Percent of college ready white graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_econ_disadv_percent = models.FloatField(
        'Percent of college ready economically disadvantaged graduates in English',
        null=True, blank=True)

    college_ready_graduates_math_all_students_percent = models.FloatField(
        'Percent of college ready students in math',
        null=True, blank=True)
    college_ready_graduates_math_african_american_percent = models.FloatField(
        'Percent of college ready African American graduates in math',
        null=True, blank=True)
    college_ready_graduates_math_american_indian_percent = models.FloatField(
        'Percent of college ready American Indian graduages in math',
        null=True, blank=True)
    college_ready_graduates_math_asian_percent = models.FloatField(
        'Percent of college ready Asian graduates in math',
        null=True, blank=True)
    college_ready_graduates_math_hispanic_percent = models.FloatField(
        'Percent of college ready Hispanic graduates in math',
        null=True, blank=True)
    college_ready_graduates_math_native_american_percent = models.FloatField(
        'Percent of college ready Native American graduates in math',
        null=True, blank=True)
    college_ready_graduates_math_pacific_islander_percent = models.FloatField(
        'Percent of college ready Pacific Islander graduates in  math',
        null=True, blank=True)
    college_ready_graduates_math_two_or_more_races_percent = models.FloatField(
        'Percent of college ready graduages of two or more races in math',
        null=True, blank=True)
    college_ready_graduates_math_white_percent = models.FloatField(
        'Percent of college ready white graduates in math',
        null=True, blank=True)
    college_ready_graduates_math_econ_disadv_percent = models.FloatField(
        'Percent of college ready economically disadvantaged graduates in math',
        null=True, blank=True)

    college_ready_graduates_both_all_students_percent = models.FloatField(
        'Percent of college ready students in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_african_american_percent = models.FloatField(
        'Percent of college ready african american graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_american_indian_percent = models.FloatField(
        'Percent of college ready American Indian graduates in borh subjects',
        null=True, blank=True)
    college_ready_graduates_both_asian_percent = models.FloatField(
        'Percent of college ready Asian graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_hispanic_percent = models.FloatField(
        'Percent of college ready Hispanic graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_native_american_percent = models.FloatField(
        'Percent of college ready Native American graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_pacific_islander_percent = models.FloatField(
        'Percent of college ready Pacific Islander graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_two_or_more_races_percent = models.FloatField(
        'Percent of college ready graduates of two or more races in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_white_percent = models.FloatField(
        'Percent of college ready white graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_econ_disadv_percent = models.FloatField(
        'Percent of college ready economically disadvantaged graduates in both subjects',
        null=True, blank=True)

    avg_sat_score_all_students = models.IntegerField(
        'Average SAT score for all students',
        null=True, blank=True)
    avg_sat_score_african_american = models.IntegerField(
        'Average SAT score for African American students',
        null=True, blank=True)
    avg_sat_score_american_indian = models.IntegerField(
        'Average SAT score for American Indian students',
        null=True, blank=True)
    avg_sat_score_asian = models.IntegerField(
        'Average SAT score for Asian students',
        null=True, blank=True)
    avg_sat_score_hispanic = models.IntegerField(
        'Average SAT score for Hispanic students',
        null=True, blank=True)
    avg_sat_score_native_american = models.IntegerField(
        'Average SAT score for Native American students',
        null=True, blank=True)
    avg_sat_score_pacific_islander = models.IntegerField(
        'Average SAT score for Pacific Islander students',
        null=True, blank=True)
    avg_sat_score_two_or_more_races = models.IntegerField(
        'Average SAT score for students of two or more races',
        null=True, blank=True)
    avg_sat_score_white = models.IntegerField(
        'Average SAT score for white students',
        null=True, blank=True)
    avg_sat_score_econ_disadv = models.IntegerField(
        'Average SAT score for economically disadvantaged students',
        null=True, blank=True)

    avg_act_score_all_students = models.FloatField(
        'Average ACT score for all students',
        null=True, blank=True)
    avg_act_score_african_american = models.FloatField(
        'Average ACT score for African American students',
        null=True, blank=True)
    avg_act_score_american_indian = models.FloatField(
        'Average ACT score for American Indian students',
        null=True, blank=True)
    avg_act_score_asian = models.FloatField(
        'Average ACT score for Asian students',
        null=True, blank=True)
    avg_act_score_hispanic = models.FloatField(
        'Average ACT score for Hispanic students',
        null=True, blank=True)
    avg_act_score_native_american = models.FloatField(
        'Average ACT score for Native American students',
        null=True, blank=True)
    avg_act_score_pacific_islander = models.FloatField(
        'Average ACT score for Pacific Islander students',
        null=True, blank=True)
    avg_act_score_two_or_more_races = models.FloatField(
        'Average ACT score for students of two or more races',
        null=True, blank=True)
    avg_act_score_white = models.FloatField(
        'Average ACT score for white students',
        null=True, blank=True)
    avg_act_score_econ_disadv = models.FloatField(
        'Average ACT score for economically disadvantaged students',
        null=True, blank=True)

    class Meta:
        abstract = True
