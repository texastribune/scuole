# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0011_auto_20150925_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionstats',
            name='attendance_rate',
            field=models.FloatField(blank=True, verbose_name='Attendance rate as calculated by students present over students in membership', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_act_score_african_american',
            field=models.FloatField(blank=True, verbose_name='Average ACT score for African American students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_act_score_all_students',
            field=models.FloatField(blank=True, verbose_name='Average ACT score for all students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_act_score_asian',
            field=models.FloatField(blank=True, verbose_name='Average ACT score for Asian students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_act_score_econ_disadv',
            field=models.FloatField(blank=True, verbose_name='Average ACT score for economically disadvantaged students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_act_score_hispanic',
            field=models.FloatField(blank=True, verbose_name='Average ACT score for Hispanic students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_act_score_native_american',
            field=models.FloatField(blank=True, verbose_name='Average ACT score for Native American students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_act_score_pacific_islander',
            field=models.FloatField(blank=True, verbose_name='Average ACT score for Pacific Islander students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_act_score_two_or_more_races',
            field=models.FloatField(blank=True, verbose_name='Average ACT score for students of two or more races', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_act_score_white',
            field=models.FloatField(blank=True, verbose_name='Average ACT score for white students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_sat_score_african_american',
            field=models.IntegerField(blank=True, verbose_name='Average SAT score for African American students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_sat_score_all_students',
            field=models.IntegerField(blank=True, verbose_name='Average SAT score for all students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_sat_score_asian',
            field=models.IntegerField(blank=True, verbose_name='Average SAT score for Asian students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_sat_score_econ_disadv',
            field=models.IntegerField(blank=True, verbose_name='Average SAT score for economically disadvantaged students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_sat_score_hispanic',
            field=models.IntegerField(blank=True, verbose_name='Average SAT score for Hispanic students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_sat_score_native_american',
            field=models.IntegerField(blank=True, verbose_name='Average SAT score for Native American students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_sat_score_pacific_islander',
            field=models.IntegerField(blank=True, verbose_name='Average SAT score for Pacific Islander students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_sat_score_two_or_more_races',
            field=models.IntegerField(blank=True, verbose_name='Average SAT score for students of two or more races', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='avg_sat_score_white',
            field=models.IntegerField(blank=True, verbose_name='Average SAT score for white students', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_african_american_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready african american graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_african_american_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready african american graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_all_students_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_all_students_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready students in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_asian_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready Asian graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_asian_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready Asian graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_at_risk_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready at risk graduates in both', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_at_risk_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready at risk graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_econ_disadv_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready economically disadvantaged graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_econ_disadv_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready economically disadvantaged graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_hispanic_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready Hispanic graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_hispanic_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready Hispanic graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_native_american_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready Native American graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_native_american_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready Native American graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_pacific_islander_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready Pacific Islander graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_pacific_islander_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready Pacific Islander graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_two_or_more_races_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready graduates of two or more races in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_two_or_more_races_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready graduates of two or more races in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_white_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready white graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_white_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready white graduates in both subjects', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_african_american_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready African American graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_african_american_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready African American graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_all_students_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready students in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_all_students_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_asian_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready Asian graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_asian_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready Asian graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_at_risk_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready at risk graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_at_risk_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready at risk graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_econ_disadv_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready economically disadvantaged graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_econ_disadv_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready economically disadvantaged graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_hispanic_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready Hispanic graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_hispanic_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready Hispanic graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_native_american_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready Native American graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_native_american_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready Native American graduates in english', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_pacific_islander_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready Pacific Islander graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_pacific_islander_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready Pacific Islander graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_two_or_more_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready graduates of two or more races in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_two_or_more_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready graduates of two or more races in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_white_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready white graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_white_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready white graduates in English', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_african_american_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready African American graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_african_american_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready African American graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_all_students_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready students in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_all_students_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready students in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_asian_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready Asian graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_asian_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready Asian graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_at_risk_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready at risk graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_at_risk_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready at risk graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_econ_disadv_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready economically disadvantaged graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_econ_disadv_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready economically disadvantaged graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_hispanic_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready Hispanic graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_hispanic_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready Hispanic graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_native_american_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready Native American graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_native_american_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready Native American graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_pacific_islander_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready Pacific Islander graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_pacific_islander_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready Pacific Islander graduates in  math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_two_or_more_races_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready graduages of two or more races in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_two_or_more_races_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready graduages of two or more races in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_white_count',
            field=models.IntegerField(blank=True, verbose_name='Number of college ready white graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_white_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of college ready white graduates in math', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_african_american_count',
            field=models.IntegerField(blank=True, verbose_name='Number of 9-12 African American students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_african_american_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of 9-12 African American students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_all_students_count',
            field=models.IntegerField(blank=True, verbose_name='Number of 9-12 students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_all_students_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of 9-12 students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_american_indian_count',
            field=models.IntegerField(blank=True, verbose_name='Number of 9-12 American Indian students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_american_indian_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of 9-12 American Indian students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_asian_count',
            field=models.IntegerField(blank=True, verbose_name='Number of 9-12 Asian students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_asian_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of 9-12 Asian students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_at_risk_count',
            field=models.IntegerField(blank=True, verbose_name='Number of 9-12 at risk students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_at_risk_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of 9-12 at risk students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_econ_disadv_count',
            field=models.IntegerField(blank=True, verbose_name='Number of 9-12 economically disadvantaged students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_econ_disadv_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of 9-12 economically disadvantaged students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_hispanic_count',
            field=models.IntegerField(blank=True, verbose_name='Number of 9-12 Hispanic students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_hispanic_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of 9-12 Hispanic students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_pacific_islander_count',
            field=models.IntegerField(blank=True, verbose_name='Number of 9-12 Pacific Islander students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_pacific_islander_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of 9-12 Pacific Islander students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_two_or_more_races_count',
            field=models.IntegerField(blank=True, verbose_name='Number of 9-12 students of two or more races who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_two_or_more_races_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of 9-12 students of two or more races who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_white_count',
            field=models.IntegerField(blank=True, verbose_name='Number of 9-12 white students who dropped out', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_white_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of 9-12 white students who dropped out', null=True),
        ),
    ]
