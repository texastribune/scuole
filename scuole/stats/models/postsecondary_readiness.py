from django.db import models


class PostSecondaryReadinessBase(models.Model):
    """
    An abstract model representing postsecondary readiness data commonly
    tracked across all entities in TEA data. Meant to be used with StatsBase
    by other apps for establishing their stats models.

    """

    # College ready counts for english
    college_ready_graduates_english_all_students_count = models.IntegerField(
        'Number of college ready students in English',
        null=True, blank=True)
    college_ready_graduates_english_african_american_count = (
        models.IntegerField(
            'Number of college ready African American graduates in English',
            null=True, blank=True))
    college_ready_graduates_english_asian_count = models.IntegerField(
        'Number of college ready Asian graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_hispanic_count = models.IntegerField(
        'Number of college ready Hispanic graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_native_american_count = (
        models.IntegerField(
            'Number of college ready Native American graduates in English',
            null=True, blank=True))
    college_ready_graduates_english_pacific_islander_count = (
        models.IntegerField(
            'Number of college ready Pacific Islander graduates in English',
            null=True, blank=True))
    college_ready_graduates_english_two_or_more_count = models.IntegerField(
        'Number of college ready graduates of two or more races in English',
        null=True, blank=True)
    college_ready_graduates_english_white_count = models.IntegerField(
        'Number of college ready white graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_econ_disadv_count = models.IntegerField(
        ('Number of college ready economically '
         'disadvantaged graduates in English'),
        null=True, blank=True)

    # College ready counts for math
    college_ready_graduates_math_all_students_count = models.IntegerField(
        'Number of college ready students in math',
        null=True, blank=True)
    college_ready_graduates_math_african_american_count = models.IntegerField(
        'Number of college ready African American graduates in math',
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

    # College ready counts for combined english and math
    college_ready_graduates_both_all_students_count = models.IntegerField(
        'Number of college ready graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_african_american_count = models.IntegerField(
        'Number of college ready african american graduates in both subjects',
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
        ('Number of college ready graduates '
         'of two or more races in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_white_count = models.IntegerField(
        'Number of college ready white graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_econ_disadv_count = models.IntegerField(
        ('Number of college ready economically '
         'disadvantaged graduates in both subjects'),
        null=True, blank=True)

    # College ready percents for english
    college_ready_graduates_english_all_students_percent = models.FloatField(
        'Percent of college ready graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_african_american_percent = (
        models.FloatField(
            'Percent of college ready African American graduates in English',
            null=True, blank=True))
    college_ready_graduates_english_asian_percent = models.FloatField(
        'Percent of college ready Asian graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_hispanic_percent = models.FloatField(
        'Percent of college ready Hispanic graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_native_american_percent = (
        models.FloatField(
            'Percent of college ready Native American graduates in english',
            null=True, blank=True))
    college_ready_graduates_english_pacific_islander_percent = (
        models.FloatField(
            'Percent of college ready Pacific Islander graduates in English',
            null=True, blank=True))
    college_ready_graduates_english_two_or_more_percent = models.FloatField(
        'Percent of college ready graduates of two or more races in English',
        null=True, blank=True)
    college_ready_graduates_english_white_percent = models.FloatField(
        'Percent of college ready white graduates in English',
        null=True, blank=True)
    college_ready_graduates_english_econ_disadv_percent = models.FloatField(
        ('Percent of college ready economically '
         'disadvantaged graduates in English'),
        null=True, blank=True)

    # college ready percents for math
    college_ready_graduates_math_all_students_percent = models.FloatField(
        'Percent of college ready students in math',
        null=True, blank=True)
    college_ready_graduates_math_african_american_percent = models.FloatField(
        'Percent of college ready African American graduates in math',
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
        'Percent of college ready economically '
        'disadvantaged graduates in math',
        null=True, blank=True)

    # college ready percents for english and math
    college_ready_graduates_both_all_students_percent = models.FloatField(
        'Percent of college ready students in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_african_american_percent = models.FloatField(
        'Percent of college ready african american graduates in both subjects',
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
        ('Percent of college ready graduates '
         'of two or more races in both subjects'),
        null=True, blank=True)
    college_ready_graduates_both_white_percent = models.FloatField(
        'Percent of college ready white graduates in both subjects',
        null=True, blank=True)
    college_ready_graduates_both_econ_disadv_percent = models.FloatField(
        ('Percent of college ready economically '
         'disadvantaged graduates in both subjects'),
        null=True, blank=True)

    # SAT scores
    avg_sat_score_all_students = models.IntegerField(
        'Average SAT score for all students',
        null=True, blank=True)
    avg_sat_score_african_american = models.IntegerField(
        'Average SAT score for African American students',
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

    # ACT scores
    avg_act_score_all_students = models.FloatField(
        'Average ACT score for all students',
        null=True, blank=True)
    avg_act_score_african_american = models.FloatField(
        'Average ACT score for African American students',
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

    dropout_all_students_count = models.IntegerField(
        'Number of 9-12 students who dropped out',
        null=True, blank=True)
    dropout_african_american_count = models.IntegerField(
        'Number of 9-12 African American students who dropped out',
        null=True, blank=True)
    dropout_american_indian_count = models.IntegerField(
        'Number of 9-12 American Indian students who dropped out',
        null=True, blank=True)
    dropout_asian_count = models.IntegerField(
        'Number of 9-12 Asian students who dropped out',
        null=True, blank=True)
    dropout_hispanic_count = models.IntegerField(
        'Number of 9-12 Hispanic students who dropped out',
        null=True, blank=True)
    dropout_pacific_islander_count = models.IntegerField(
        'Number of 9-12 Pacific Islander students who dropped out',
        null=True, blank=True)
    dropout_two_or_more_races_count = models.IntegerField(
        'Number of 9-12 students of two or more races who dropped out',
        null=True, blank=True)
    dropout_white_count = models.IntegerField(
        'Number of 9-12 white students who dropped out',
        null=True, blank=True)
    dropout_white_count = models.IntegerField(
        'Number of 9-12 white students who dropped out',
        null=True, blank=True)
    dropout_at_risk_count = models.IntegerField(
        'Number of 9-12 at risk students who dropped out',
        null=True, blank=True)
    dropout_econ_disadv_count = models.IntegerField(
        'Number of 9-12 economically disadvantaged students who dropped out',
        null=True, blank=True)

    dropout_all_students_percent = models.FloatField(
        'Percent of 9-12 students who dropped out',
        null=True, blank=True)
    dropout_african_american_percent = models.FloatField(
        'Percent of 9-12 African American students who dropped out',
        null=True, blank=True)
    dropout_american_indian_percent = models.FloatField(
        'Percent of 9-12 American Indian students who dropped out',
        null=True, blank=True)
    dropout_asian_percent = models.FloatField(
        'Percent of 9-12 Asian students who dropped out',
        null=True, blank=True)
    dropout_hispanic_percent = models.FloatField(
        'Percent of 9-12 Hispanic students who dropped out',
        null=True, blank=True)
    dropout_pacific_islander_percent = models.FloatField(
        'Percent of 9-12 Pacific Islander students who dropped out',
        null=True, blank=True)
    dropout_two_or_more_races_percent = models.FloatField(
        'Percent of 9-12 students of two or more races who dropped out',
        null=True, blank=True)
    dropout_white_percent = models.FloatField(
        'Percent of 9-12 white students who dropped out',
        null=True, blank=True)
    dropout_at_risk_percent = models.FloatField(
        'Percent of 9-12 at risk students who dropped out',
        null=True, blank=True)
    dropout_econ_disadv_percent = models.FloatField(
        'Percent of 9-12 economically disadvantaged students who dropped out',
        null=True, blank=True)


    class Meta:
        abstract = True
