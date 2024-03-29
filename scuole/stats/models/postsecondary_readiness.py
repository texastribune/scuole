# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class PostSecondaryReadinessBase(models.Model):
    """
    An abstract model representing postsecondary readiness data commonly
    tracked across all entities in TEA data. Meant to be used with StatsBase
    by other apps for establishing their stats models.

    """

    # College ready counts for english
    college_ready_graduates_english_all_students_count = models.IntegerField(
        _('Number of college ready students in English'),
        null=True, blank=True)
    college_ready_graduates_english_african_american_count = (
        models.IntegerField(
            _('Number of college ready African American graduates in English'),
            null=True, blank=True))
    college_ready_graduates_english_asian_count = models.IntegerField(
        _('Number of college ready Asian graduates in English'),
        null=True, blank=True)
    college_ready_graduates_english_hispanic_count = models.IntegerField(
        _('Number of college ready Hispanic graduates in English'),
        null=True, blank=True)
    college_ready_graduates_english_american_indian_count = (
        models.IntegerField(
            _('Number of college ready American Indian graduates in English'),
            null=True, blank=True))
    college_ready_graduates_english_pacific_islander_count = (
        models.IntegerField(
            _('Number of college ready Pacific Islander graduates in English'),
            null=True, blank=True))
    college_ready_graduates_english_two_or_more_races_count = models.IntegerField(
        _('Number of college ready graduates of two or more races in English'),
        null=True, blank=True)
    college_ready_graduates_english_white_count = models.IntegerField(
        _('Number of college ready white graduates in English'),
        null=True, blank=True)
    college_ready_graduates_english_economically_disadvantaged_count = (
        models.IntegerField(
            _('Number of college ready economically '
              'disadvantaged graduates in English'),
            null=True, blank=True,
            db_column='college_ready_graduates_english_econ_disadv_count'))
    college_ready_graduates_english_limited_english_proficient_count = (
        models.IntegerField(
            _('Number of college ready limited english '
              'proficient graduates in English'),
            null=True, blank=True,
            db_column='college_ready_graduates_english_lep_count'))
    college_ready_graduates_english_at_risk_count = models.IntegerField(
        _('Number of college ready at risk graduates in English'),
        null=True, blank=True)

    # College ready counts for math
    college_ready_graduates_math_all_students_count = models.IntegerField(
        _('Number of college ready students in math'),
        null=True, blank=True)
    college_ready_graduates_math_african_american_count = models.IntegerField(
        _('Number of college ready African American graduates in math'),
        null=True, blank=True)
    college_ready_graduates_math_asian_count = models.IntegerField(
        _('Number of college ready Asian graduates in math'),
        null=True, blank=True)
    college_ready_graduates_math_hispanic_count = models.IntegerField(
        _('Number of college ready Hispanic graduates in math'),
        null=True, blank=True)
    college_ready_graduates_math_american_indian_count = models.IntegerField(
        _('Number of college ready American Indian graduates in math'),
        null=True, blank=True)
    college_ready_graduates_math_pacific_islander_count = models.IntegerField(
        _('Number of college ready Pacific Islander graduates in math'),
        null=True, blank=True)
    college_ready_graduates_math_two_or_more_races_count = models.IntegerField(
        _('Number of college ready graduages of two or more races in math'),
        null=True, blank=True)
    college_ready_graduates_math_white_count = models.IntegerField(
        _('Number of college ready white graduates in math'),
        null=True, blank=True)
    college_ready_graduates_math_economically_disadvantaged_count = (
        models.IntegerField(
            _('Number of college ready economically disadvantaged graduates in math'),
            null=True, blank=True,
            db_column='college_ready_graduates_math_econ_disadv_count'))
    college_ready_graduates_math_limited_english_proficient_count = (
        models.IntegerField(
            _('Number of college ready limited english '
              'proficient graduates in math'),
            null=True, blank=True,
            db_column='college_ready_graduates_math_lep_count'))
    college_ready_graduates_math_at_risk_count = models.IntegerField(
        _('Number of college ready at risk graduates in math'),
        null=True, blank=True)

    # College ready counts for combined english and math
    college_ready_graduates_both_all_students_count = models.IntegerField(
        _('Number of college ready graduates in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_african_american_count = models.IntegerField(
        _('Number of college ready african american graduates in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_asian_count = models.IntegerField(
        _('Number of college ready Asian graduates in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_hispanic_count = models.IntegerField(
        _('Number of college ready Hispanic graduates in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_american_indian_count = models.IntegerField(
        _('Number of college ready American Indian graduates in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_pacific_islander_count = models.IntegerField(
        _('Number of college ready Pacific Islander graduates in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_two_or_more_races_count = models.IntegerField(
        _('Number of college ready graduates '
         'of two or more races in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_white_count = models.IntegerField(
        _('Number of college ready white graduates in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_economically_disadvantaged_count = (
        models.IntegerField(
            _('Number of college ready economically '
              'disadvantaged graduates in both subjects'),
            null=True, blank=True,
            db_column='college_ready_graduates_both_econ_disadv_count'))
    college_ready_graduates_both_limited_english_proficient_count = (
        models.IntegerField(
            _('Number of college ready limited english '
              'proficient graduates in both subjects'),
            null=True, blank=True,
            db_column='college_ready_graduates_both_lep_count'))
    college_ready_graduates_both_at_risk_count = models.IntegerField(
        _('Number of college ready at risk graduates in both'),
        null=True, blank=True)

    # College ready percents for english
    college_ready_graduates_english_all_students_percent = models.FloatField(
        _('Percent of college ready graduates in English'),
        null=True, blank=True)
    college_ready_graduates_english_african_american_percent = (
        models.FloatField(
            _('Percent of college ready African American graduates in English'),
            null=True, blank=True))
    college_ready_graduates_english_asian_percent = models.FloatField(
        _('Percent of college ready Asian graduates in English'),
        null=True, blank=True)
    college_ready_graduates_english_hispanic_percent = models.FloatField(
        _('Percent of college ready Hispanic graduates in English'),
        null=True, blank=True)
    college_ready_graduates_english_american_indian_percent = (
        models.FloatField(
            _('Percent of college ready American Indian graduates in english'),
            null=True, blank=True))
    college_ready_graduates_english_pacific_islander_percent = (
        models.FloatField(
            _('Percent of college ready Pacific Islander graduates in English'),
            null=True, blank=True))
    college_ready_graduates_english_two_or_more_races_percent = models.FloatField(
        _('Percent of college ready graduates of two or more races in English'),
        null=True, blank=True)
    college_ready_graduates_english_white_percent = models.FloatField(
        _('Percent of college ready white graduates in English'),
        null=True, blank=True)
    college_ready_graduates_english_economically_disadvantaged_percent = (
        models.FloatField(
            _('Percent of college ready economically '
              'disadvantaged graduates in English'),
            null=True, blank=True,
            db_column='college_ready_graduates_english_econ_disadv_percent'))
    college_ready_graduates_english_limited_english_proficient_percent = (
        models.FloatField(
            _('Percent of college ready limited english '
              'proficient graduates in English'),
            null=True, blank=True,
            db_column='college_ready_graduates_english_lep_percent'))
    college_ready_graduates_english_at_risk_percent = models.FloatField(
        _('Percent of college ready at risk graduates in English'),
        null=True, blank=True)

    # college ready percents for math
    college_ready_graduates_math_all_students_percent = models.FloatField(
        _('Percent of college ready students in math'),
        null=True, blank=True)
    college_ready_graduates_math_african_american_percent = models.FloatField(
        _('Percent of college ready African American graduates in math'),
        null=True, blank=True)
    college_ready_graduates_math_asian_percent = models.FloatField(
        _('Percent of college ready Asian graduates in math'),
        null=True, blank=True)
    college_ready_graduates_math_hispanic_percent = models.FloatField(
        _('Percent of college ready Hispanic graduates in math'),
        null=True, blank=True)
    college_ready_graduates_math_american_indian_percent = models.FloatField(
        _('Percent of college ready American Indian graduates in math'),
        null=True, blank=True)
    college_ready_graduates_math_pacific_islander_percent = models.FloatField(
        _('Percent of college ready Pacific Islander graduates in math'),
        null=True, blank=True)
    college_ready_graduates_math_two_or_more_races_percent = models.FloatField(
        _('Percent of college ready graduages of two or more races in math'),
        null=True, blank=True)
    college_ready_graduates_math_white_percent = models.FloatField(
        _('Percent of college ready white graduates in math'),
        null=True, blank=True)
    college_ready_graduates_math_economically_disadvantaged_percent = (
        models.FloatField(
            _('Percent of college ready economically '
              'disadvantaged graduates in math'),
            null=True, blank=True,
            db_column='college_ready_graduates_math_econ_disadv_percent'))
    college_ready_graduates_math_limited_english_proficient_percent = (
        models.FloatField(
            _('Percent of college ready limited english '
              'proficient graduates in math'),
            null=True, blank=True,
            db_column='college_ready_graduates_math_lep_percent'))
    college_ready_graduates_math_at_risk_percent = models.FloatField(
        _('Percent of college ready at risk graduates in math'),
        null=True, blank=True)

    # college ready percents for english and math
    college_ready_graduates_both_all_students_percent = models.FloatField(
        _('Percent of college ready students in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_african_american_percent = models.FloatField(
        _('Percent of college ready african american graduates in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_asian_percent = models.FloatField(
        _('Percent of college ready Asian graduates in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_hispanic_percent = models.FloatField(
        _('Percent of college ready Hispanic graduates in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_american_indian_percent = models.FloatField(
        _('Percent of college ready American Indian graduates in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_pacific_islander_percent = models.FloatField(
        _('Percent of college ready Pacific Islander graduates in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_two_or_more_races_percent = models.FloatField(
        _('Percent of college ready graduates '
          'of two or more races in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_white_percent = models.FloatField(
        _('Percent of college ready white graduates in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_economically_disadvantaged_percent = (
        models.FloatField(
            _('Percent of college ready economically '
              'disadvantaged graduates in both subjects'),
            null=True, blank=True,
            db_column='college_ready_graduates_both_econ_disadv_percent'))
    college_ready_graduates_both_limited_english_proficient_percent = (
        models.FloatField(
            _('Percent of college ready limited english '
              'proficient graduates in both subjects'),
            null=True, blank=True,
            db_column='college_ready_graduates_both_lep_percent'))
    college_ready_graduates_both_at_risk_percent = models.FloatField(
        _('Percent of college ready at risk graduates in both subjects'),
        null=True, blank=True)

    # SAT scores
    avg_sat_score_all_students = models.IntegerField(
        _('Average SAT score for all students'),
        null=True, blank=True)
    avg_sat_score_african_american = models.IntegerField(
        _('Average SAT score for African American students'),
        null=True, blank=True)
    avg_sat_score_asian = models.IntegerField(
        _('Average SAT score for Asian students'),
        null=True, blank=True)
    avg_sat_score_hispanic = models.IntegerField(
        _('Average SAT score for Hispanic students'),
        null=True, blank=True)
    avg_sat_score_american_indian = models.IntegerField(
        _('Average SAT score for American Indian students'),
        null=True, blank=True)
    avg_sat_score_pacific_islander = models.IntegerField(
        _('Average SAT score for Pacific Islander students'),
        null=True, blank=True)
    avg_sat_score_two_or_more_races = models.IntegerField(
        _('Average SAT score for students of two or more races'),
        null=True, blank=True)
    avg_sat_score_white = models.IntegerField(
        _('Average SAT score for white students'),
        null=True, blank=True)
    avg_sat_score_economically_disadvantaged = models.IntegerField(
        _('Average SAT score for economically disadvantaged students'),
        null=True, blank=True)

    # ACT scores
    avg_act_score_all_students = models.FloatField(
        _('Average ACT score for all students'),
        null=True, blank=True)
    avg_act_score_african_american = models.FloatField(
        _('Average ACT score for African American students'),
        null=True, blank=True)
    avg_act_score_asian = models.FloatField(
        _('Average ACT score for Asian students'),
        null=True, blank=True)
    avg_act_score_hispanic = models.FloatField(
        _('Average ACT score for Hispanic students'),
        null=True, blank=True)
    avg_act_score_american_indian = models.FloatField(
        _('Average ACT score for American Indian students'),
        null=True, blank=True)
    avg_act_score_pacific_islander = models.FloatField(
        _('Average ACT score for Pacific Islander students'),
        null=True, blank=True)
    avg_act_score_two_or_more_races = models.FloatField(
        _('Average ACT score for students of two or more races'),
        null=True, blank=True)
    avg_act_score_white = models.FloatField(
        _('Average ACT score for white students'),
        null=True, blank=True)
    avg_act_score_economically_disadvantaged = models.FloatField(
        _('Average ACT score for economically disadvantaged students'),
        null=True, blank=True)

    ap_ib_all_students_count_above_criterion = models.IntegerField(
        _('Number of students who scored above criterion on'
          'at least one AP or IB test'), null=True, blank=True)
    ap_ib_african_american_count_above_criterion = models.IntegerField(
        _('Number of African American students who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_asian_count_above_criterion = models.IntegerField(
        _('Number of Asian students who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_hispanic_count_above_criterion = models.IntegerField(
        _('Number of Hispanic students who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_american_indian_count_above_criterion = models.IntegerField(
        _('Number of American Insian students who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_pacific_islander_count_above_criterion = models.IntegerField(
        _('Number of Pacific Islander students who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_two_or_more_races_count_above_criterion = models.IntegerField(
        _('Number of students of two or more races who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_white_count_above_criterion = models.IntegerField(
        _('Number of white students who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_economically_disadvantaged_count_above_criterion = (
        models.IntegerField(
            _('Number of white students who scored above'
              'criterion on at least one AP or IB test'),
            null=True, blank=True))

    ap_ib_all_students_percent_above_criterion = models.FloatField(
        _('Percent of students who scored above criterion on'
          'at least one AP or IB test'), null=True, blank=True)
    ap_ib_african_american_percent_above_criterion = models.FloatField(
        _('Percent of African American students who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_asian_percent_above_criterion = models.FloatField(
        _('Percent of Asian students who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_hispanic_percent_above_criterion = models.FloatField(
        _('Percent of Hispanic students who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_american_indian_percent_above_criterion = models.FloatField(
        _('Percent of American Insian students who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_pacific_islander_percent_above_criterion = models.FloatField(
        _('Percent of Pacific Islander students who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_two_or_more_races_percent_above_criterion = models.FloatField(
        _('Percent of students of two or more races who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_white_percent_above_criterion = models.FloatField(
        _('Percent of white students who scored above'
          'criterion on at least one AP or IB test'), null=True, blank=True)
    ap_ib_economically_disadvantaged_percent_above_criterion = (
        models.FloatField(
            _('Percent of economically disadvantaged students who'
              'scored above criterion on at least one AP or IB test'),
            null=True, blank=True))

    ap_ib_all_students_percent_taking = models.FloatField(
        _('Percent of students taking at least one'
          'AP or IB test'), null=True, blank=True)
    ap_ib_african_american_percent_taking = models.FloatField(
        _('Percent of African American students taking at least one'
          'AP or IB test'), null=True, blank=True)
    ap_ib_asian_percent_taking = models.FloatField(
        _('Percent of Asian students taking at least one'
          'AP or IB test'), null=True, blank=True)
    ap_ib_hispanic_percent_taking = models.FloatField(
        _('Percent of Hispanic students taking at least one'
          'AP or IB test'), null=True, blank=True)
    ap_ib_american_indian_percent_taking = models.FloatField(
        _('Percent of American Insian students taking at least one'
          'AP or IB test'), null=True, blank=True)
    ap_ib_pacific_islander_percent_taking = models.FloatField(
        _('Percent of Pacific Islander students taking at least one'
          'AP or IB test'), null=True, blank=True)
    ap_ib_two_or_more_races_percent_taking = models.FloatField(
        _('Percent of students of two or more races taking at least one'
          'AP or IB test'), null=True, blank=True)
    ap_ib_white_percent_taking = models.FloatField(
        _('Percent of white students taking at least one'
          'AP or IB test'), null=True, blank=True)
    ap_ib_economically_disadvantaged_percent_taking = (
        models.FloatField(
            _('Percent of economically disadvantaged students taking'
              'at least one AP or IB test'),
            null=True, blank=True))

    dropout_all_students_count = models.IntegerField(
        _('Number of 9-12 students who dropped out'),
        null=True, blank=True)
    dropout_african_american_count = models.IntegerField(
        _('Number of 9-12 African American students who dropped out'),
        null=True, blank=True)
    dropout_american_indian_count = models.IntegerField(
        _('Number of 9-12 American Indian students who dropped out'),
        null=True, blank=True)
    dropout_asian_count = models.IntegerField(
        _('Number of 9-12 Asian students who dropped out'),
        null=True, blank=True)
    dropout_hispanic_count = models.IntegerField(
        _('Number of 9-12 Hispanic students who dropped out'),
        null=True, blank=True)
    dropout_pacific_islander_count = models.IntegerField(
        _('Number of 9-12 Pacific Islander students who dropped out'),
        null=True, blank=True)
    dropout_two_or_more_races_count = models.IntegerField(
        _('Number of 9-12 students of two or more races who dropped out'),
        null=True, blank=True)
    dropout_white_count = models.IntegerField(
        _('Number of 9-12 white students who dropped out'),
        null=True, blank=True)
    dropout_at_risk_count = models.IntegerField(
        _('Number of 9-12 white students who dropped out'),
        null=True, blank=True)
    dropout_economically_disadvantaged_count = models.IntegerField(
        _('Number of 9-12 economically disadvantaged students who dropped out'),
        null=True, blank=True)
    dropout_limited_english_proficient_count = models.IntegerField(
        _('Number of 9-12 limited English proficient students who dropped out'),
        null=True, blank=True)

    dropout_all_students_percent = models.FloatField(
        _('Percent of 9-12 students who dropped out'),
        null=True, blank=True)
    dropout_african_american_percent = models.FloatField(
        _('Percent of 9-12 African American students who dropped out'),
        null=True, blank=True)
    dropout_american_indian_percent = models.FloatField(
        _('Percent of 9-12 American Indian students who dropped out'),
        null=True, blank=True)
    dropout_asian_percent = models.FloatField(
        _('Percent of 9-12 Asian students who dropped out'),
        null=True, blank=True)
    dropout_hispanic_percent = models.FloatField(
        _('Percent of 9-12 Hispanic students who dropped out'),
        null=True, blank=True)
    dropout_pacific_islander_percent = models.FloatField(
        _('Percent of 9-12 Pacific Islander students who dropped out'),
        null=True, blank=True)
    dropout_two_or_more_races_percent = models.FloatField(
        _('Percent of 9-12 students of two or more races who dropped out'),
        null=True, blank=True)
    dropout_white_percent = models.FloatField(
        _('Percent of 9-12 white students who dropped out'),
        null=True, blank=True)
    dropout_at_risk_percent = models.FloatField(
        _('Percent of 9-12 at risk students who dropped out'),
        null=True, blank=True)
    dropout_economically_disadvantaged_percent = models.FloatField(
        _('Percent of 9-12 economically disadvantaged students who dropped out'),
        null=True, blank=True)
    dropout_limited_english_proficient_percent = models.FloatField(
        _('Percent of 9-12 limited English proficient students who dropped out'),
        null=True, blank=True)

    four_year_graduate_all_students_count = models.IntegerField(
        _('Number of students who graduated in 4 years'), null=True, blank=True)
    four_year_graduate_african_american_count = models.IntegerField(
        _('Number of African American students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_american_indian_count = models.IntegerField(
        _('Number of American Indian students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_asian_count = models.IntegerField(
        _('Number of Asian students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_hispanic_count = models.IntegerField(
        _('Number of Hispanic students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_pacific_islander_count = models.IntegerField(
        _('Number of Pacific Islander students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_two_or_more_races_count = models.IntegerField(
        _('Number of students of two or more races who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_white_count = models.IntegerField(
        _('Number of white students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_at_risk_count = models.IntegerField(
        _('Number of at risk students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_economically_disadvantaged_count = models.IntegerField(
        _('Number of economically disadvantaged students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_limited_english_proficient_count = models.IntegerField(
        _('Number of limited English proficient students who graduated in 4 years'),
        null=True, blank=True)

    four_year_graduate_all_students_percent = models.FloatField(
        _('Percent of students who graduated in 4 years'), null=True, blank=True)
    four_year_graduate_african_american_percent = models.FloatField(
        _('Percent of African American students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_american_indian_percent = models.FloatField(
        _('Percent of American Indian students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_asian_percent = models.FloatField(
        _('Percent of Asian students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_hispanic_percent = models.FloatField(
        _('Percent of Hispanic students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_pacific_islander_percent = models.FloatField(
        _('Percent of Pacific Islander students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_two_or_more_races_percent = models.FloatField(
        _('Percent of students of two or more races who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_white_percent = models.FloatField(
        _('Percent of white students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_at_risk_percent = models.FloatField(
        _('Percent of at risk students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_economically_disadvantaged_percent = models.FloatField(
        _('Percent of economically disadvantaged students who graduated in 4 years'),
        null=True, blank=True)
    four_year_graduate_limited_english_proficient_percent = models.FloatField(
        _('Percent of limited English proficient students who graduated in 4 years'),
        null=True, blank=True)

    attendance_rate = models.FloatField(
        _('Attendance rate as calculated by '
          'students present over students in membership'),
        null=True, blank=True)

    chronic_absenteeism_all_students_percent = models.FloatField(
        _('Chronic absenteeism rate as calculated by '
          'students chronically absent over students in membership'),
        null=True, blank=True)

    chronic_absenteeism_african_american_percent = models.FloatField(
        _('Chronic absenteeism rate as calculated by '
          'African American students chronically absent over students in membership'),
        null=True, blank=True)

    chronic_absenteeism_asian_percent = models.FloatField(
        _('Chronic absenteeism rate as calculated by '
          'Asian students chronically absent over students in membership'),
        null=True, blank=True)

    chronic_absenteeism_hispanic_percent = models.FloatField(
        _('Chronic absenteeism rate as calculated by '
          'Hispanic students chronically absent over students in membership'),
        null=True, blank=True)

    chronic_absenteeism_american_indian_percent = models.FloatField(
        _('Chronic absenteeism rate as calculated by '
          'American Indian students chronically absent over students in membership'),
        null=True, blank=True)

    chronic_absenteeism_pacific_islander_percent = models.FloatField(
        _('Chronic absenteeism rate as calculated by '
          'Pacific Islander students chronically absent over students in membership'),
        null=True, blank=True)

    chronic_absenteeism_two_or_more_races_percent = models.FloatField(
        _('Chronic absenteeism rate as calculated by '
          'students of two or more races chronically absent over students in membership'),
        null=True, blank=True)

    chronic_absenteeism_white_percent = models.FloatField(
        _('Chronic absenteeism rate as calculated by '
          'White students chronically absent over students in membership'),
        null=True, blank=True)

    class Meta:
        abstract = True

    def get_percentages_for_all_races(self, field_template):
        races = (
            ('African American', 'african_american'),
            ('American Indian', 'american_indian'),
            ('Asian', 'asian'),
            ('Hispanic', 'hispanic'),
            ('Pacific Islander', 'pacific_islander'),
            ('White', 'white'),
            ('Two or More Races', 'two_or_more_races'),
        )

        payload = []

        for race in races:
            field = getattr(self, field_template.format(race[1]))

            payload.append({
                'name': race[0],
                'value': field
            })

        return payload

    @property
    def four_year_graduate_percent(self):
        return self.get_percentages_for_all_races(
            'four_year_graduate_{}_percent')

    @property
    def college_readiness_percents(self):
        return [{
            'name': 'Reading',
            'value': self.college_ready_graduates_english_all_students_percent
        }, {
            'name': 'Math',
            'value': self.college_ready_graduates_math_all_students_percent
        }, {
            'name': 'Reading + Math',
            'value': self.college_ready_graduates_both_all_students_percent
        }]
