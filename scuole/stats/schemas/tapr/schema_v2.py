SCHEMA = {
    # staff-and-student-information
    "all_students_count": "{short_code}PETALLC",
    "african_american_count": "{short_code}PETBLAC",
    "african_american_percent": "{short_code}PETBLAP",
    "american_indian_count": "{short_code}PETINDC",
    "american_indian_percent": "{short_code}PETINDP",
    "asian_count": "{short_code}PETASIC",
    "asian_percent": "{short_code}PETASIP",
    "hispanic_count": "{short_code}PETHISC",
    "hispanic_percent": "{short_code}PETHISP",
    "pacific_islander_count": "{short_code}PETPCIC",
    "pacific_islander_percent": "{short_code}PETPCIP",
    "two_or_more_races_count": "{short_code}PETTWOC",
    "two_or_more_races_percent": "{short_code}PETTWOP",
    "white_count": "{short_code}PETWHIC",
    "white_percent": "{short_code}PETWHIP",
    "early_childhood_education_count": "{short_code}PETGEEC",
    "early_childhood_education_percent": "{short_code}PETGEEP",
    "prek_count": "{short_code}PETGPKC",
    "prek_percent": "{short_code}PETGPKP",
    "kindergarten_count": "{short_code}PETGKNC",
    "kindergarten_percent": "{short_code}PETGKNP",
    "first_count": "{short_code}PETG01C",
    "first_percent": "{short_code}PETG01P",
    "second_count": "{short_code}PETG02C",
    "second_percent": "{short_code}PETG02P",
    "third_count": "{short_code}PETG03C",
    "third_percent": "{short_code}PETG03P",
    "fourth_count": "{short_code}PETG04C",
    "fourth_percent": "{short_code}PETG04P",
    "fifth_count": "{short_code}PETG05C",
    "fifth_percent": "{short_code}PETG05P",
    "sixth_count": "{short_code}PETG06C",
    "sixth_percent": "{short_code}PETG06P",
    "seventh_count": "{short_code}PETG07C",
    "seventh_percent": "{short_code}PETG07P",
    "eighth_count": "{short_code}PETG08C",
    "eighth_percent": "{short_code}PETG08P",
    "ninth_count": "{short_code}PETG09C",
    "ninth_percent": "{short_code}PETG09P",
    "tenth_count": "{short_code}PETG10C",
    "tenth_percent": "{short_code}PETG10P",
    "eleventh_count": "{short_code}PETG11C",
    "eleventh_percent": "{short_code}PETG11P",
    "twelfth_count": "{short_code}PETG12C",
    "twelfth_percent": "{short_code}PETG12P",
    "at_risk_count": "{short_code}PETRSKC",
    "at_risk_percent": "{short_code}PETRSKP",
    "economically_disadvantaged_count": "{short_code}PETECOC",
    "economically_disadvantaged_percent": "{short_code}PETECOP",
    "limited_english_proficient_count": "{short_code}PETLEPC",
    "limited_english_proficient_percent": "{short_code}PETLEPP",
    "bilingual_esl_count": "{short_code}PETBILC",
    "bilingual_esl_percent": "{short_code}PETBILP",
    "career_technical_education_count": "{short_code}PETVOCC",
    "career_technical_education_percent": "{short_code}PETVOCP",
    "gifted_and_talented_count": "{short_code}PETGIFC",
    "gifted_and_talented_percent": "{short_code}PETGIFP",
    "special_education_count": "{short_code}PETSPEC",
    "special_education_percent": "{short_code}PETSPEP",
    "class_size_avg_kindergarten": "{short_code}PCTGKGA",
    "class_size_avg_first": "{short_code}PCTG01A",
    "class_size_avg_second": "{short_code}PCTG02A",
    "class_size_avg_third": "{short_code}PCTG03A",
    "class_size_avg_fourth": "{short_code}PCTG04A",
    "class_size_avg_fifth": "{short_code}PCTG05A",
    "class_size_avg_sixth": "{short_code}PCTG06A",
    "class_size_avg_mixed_elementary": "{short_code}PCTGMEA",
    "class_size_avg_secondary_english": "{short_code}PCTENGA",
    "class_size_avg_secondary_foreign_language": "{short_code}PCTFLAA",
    "class_size_avg_secondary_math": "{short_code}PCTMATA",
    "class_size_avg_secondary_science": "{short_code}PCTSCIA",
    "class_size_avg_secondary_social_studies": "{short_code}PCTSOCA",
    "students_per_teacher": "{short_code}PSTKIDR",
    # teacher_avg_tenure is Average Years Experience of Teachers with District
    "teacher_avg_tenure": "{short_code}PSTTENA",
    # teacher_avg_experience is Average Years Experience of Teachers
    "teacher_avg_experience": "{short_code}PSTEXPA",
    "teacher_avg_base_salary": "{short_code}PSTTOSA",
    "teacher_avg_beginning_salary": "{short_code}PST00SA",
    "teacher_avg_1_to_5_year_salary": "{short_code}PST01SA",
    "teacher_avg_6_to_10_year_salary": "{short_code}PST06SA",
    "teacher_avg_11_to_20_year_salary": "{short_code}PST11SA",
    "teacher_avg_20_plus_year_salary": "{short_code}PST20SA",
    "teacher_total_fte_count": "{short_code}PSTTOFC",
    "teacher_african_american_fte_count": "{short_code}PSTBLFC",
    "teacher_american_indian_fte_count": "{short_code}PSTINFC",
    "teacher_asian_fte_count": "{short_code}PSTASFC",
    "teacher_hispanic_fte_count": "{short_code}PSTHIFC",
    "teacher_pacific_islander_fte_count": "{short_code}PSTPIFC",
    "teacher_two_or_more_races_fte_count": "{short_code}PSTTWFC",
    "teacher_white_fte_count": "{short_code}PSTWHFC",
    "teacher_total_fte_percent": "{short_code}PSTTOFC",
    "teacher_african_american_fte_percent": "{short_code}PSTBLFP",
    "teacher_american_indian_fte_percent": "{short_code}PSTINFP",
    "teacher_asian_fte_percent": "{short_code}PSTASFP",
    "teacher_hispanic_fte_percent": "{short_code}PSTHIFP",
    "teacher_pacific_islander_fte_percent": "{short_code}PSTPIFP",
    "teacher_two_or_more_races_fte_percent": "{short_code}PSTTWFP",
    "teacher_white_fte_percent": "{short_code}PSTWHFP",
    "teacher_no_degree_count": "{short_code}PSTNOFC",
    "teacher_bachelors_count": "{short_code}PSTBAFC",
    "teacher_masters_count": "{short_code}PSTMSFC",
    "teacher_doctorate_count": "{short_code}PSTPHFC",
    "teacher_no_degree_percent": "{short_code}PSTNOFP",
    "teacher_bachelors_percent": "{short_code}PSTBAFP",
    "teacher_masters_percent": "{short_code}PSTMSFP",
    "teacher_doctorate_percent": "{short_code}PSTPHFP",
    # postsecondary-readiness-and-non-staar-performance-indicators
    # 'college_ready_graduates_english_all_students_count': 'ACRR',
    "college_ready_graduates_english_all_students_percent": "{short_code}ACRR{year}R",
    # 'college_ready_graduates_english_african_american_count': 'BCRR',
    "college_ready_graduates_english_african_american_percent": "{short_code}BCRR{year}R",
    # 'college_ready_graduates_english_american_indian_count': 'ICRR',
    "college_ready_graduates_english_american_indian_percent": "{short_code}ICRR{year}R",
    # 'college_ready_graduates_english_asian_count': '3CRR',
    "college_ready_graduates_english_asian_percent": "{short_code}3CRR{year}R",
    # 'college_ready_graduates_english_hispanic_count': 'HCRR',
    "college_ready_graduates_english_hispanic_percent": "{short_code}HCRR{year}R",
    # 'college_ready_graduates_english_pacific_islander_count': '4CRR',
    "college_ready_graduates_english_pacific_islander_percent": "{short_code}4CRR{year}R",
    # 'college_ready_graduates_english_two_or_more_races_count': '2CRR',
    "college_ready_graduates_english_two_or_more_races_percent": "{short_code}2CRR{year}R",
    # 'college_ready_graduates_english_white_count': 'WCRR',
    "college_ready_graduates_english_white_percent": "{short_code}WCRR{year}R",
    # 'college_ready_graduates_english_economically_disadvantaged_count': 'ECRR',
    "college_ready_graduates_english_economically_disadvantaged_percent": "{short_code}ECRR{year}R",
    # 'college_ready_graduates_english_limited_english_proficient_count': 'LCRR',
    "college_ready_graduates_english_limited_english_proficient_percent": "{short_code}LCRR{year}R",
    # 'college_ready_graduates_english_at_risk_count': 'RCRR',
    "college_ready_graduates_english_at_risk_percent": "{short_code}RCRR{year}R",
    # 'college_ready_graduates_math_all_students_count': 'ACRM',
    "college_ready_graduates_math_all_students_percent": "{short_code}ACRM{year}R",
    # 'college_ready_graduates_math_african_american_count': 'BCRM',
    "college_ready_graduates_math_african_american_percent": "{short_code}BCRM{year}R",
    # 'college_ready_graduates_math_american_indian_count': 'ICRM',
    "college_ready_graduates_math_american_indian_percent": "{short_code}ICRM{year}R",
    # 'college_ready_graduates_math_asian_count': '3CRM',
    "college_ready_graduates_math_asian_percent": "{short_code}3CRM{year}R",
    # 'college_ready_graduates_math_hispanic_count': 'HCRM',
    "college_ready_graduates_math_hispanic_percent": "{short_code}HCRM{year}R",
    # 'college_ready_graduates_math_pacific_islander_count': '4CRM',
    "college_ready_graduates_math_pacific_islander_percent": "{short_code}4CRM{year}R",
    # 'college_ready_graduates_math_two_or_more_races_count': '2CRM',
    "college_ready_graduates_math_two_or_more_races_percent": "{short_code}2CRM{year}R",
    # 'college_ready_graduates_math_white_count': 'WCRM',
    "college_ready_graduates_math_white_percent": "{short_code}WCRM{year}R",
    # 'college_ready_graduates_math_economically_disadvantaged_count': 'ECRM',
    "college_ready_graduates_math_economically_disadvantaged_percent": "{short_code}ECRM{year}R",
    # 'college_ready_graduates_math_limited_english_proficient_count': 'LCRM',
    "college_ready_graduates_math_limited_english_proficient_percent": "{short_code}LCRM{year}R",
    # 'college_ready_graduates_math_at_risk_count': 'RCRM',
    "college_ready_graduates_math_at_risk_percent": "{short_code}RCRM{year}R",
    # 'college_ready_graduates_both_all_students_count': 'ACRB',
    "college_ready_graduates_both_all_students_percent": "{short_code}ACRB{year}R",
    # 'college_ready_graduates_both_african_american_count': 'BCRB',
    "college_ready_graduates_both_african_american_percent": "{short_code}BCRB{year}R",
    # 'college_ready_graduates_both_asian_count': '3CRB',
    "college_ready_graduates_both_asian_percent": "{short_code}3CRB{year}R",
    # 'college_ready_graduates_both_hispanic_count': 'HCRB',
    "college_ready_graduates_both_hispanic_percent": "{short_code}HCRB{year}R",
    # 'college_ready_graduates_both_american_indian_count': 'ICRB',
    "college_ready_graduates_both_american_indian_percent": "{short_code}ICRB{year}R",
    # 'college_ready_graduates_both_pacific_islander_count': '4CRB',
    "college_ready_graduates_both_pacific_islander_percent": "{short_code}4CRB{year}R",
    # 'college_ready_graduates_both_two_or_more_races_count': '2CRB',
    "college_ready_graduates_both_two_or_more_races_percent": "{short_code}2CRB{year}R",
    # 'college_ready_graduates_both_white_count': 'WCRB',
    "college_ready_graduates_both_white_percent": "{short_code}WCRB{year}R",
    # 'college_ready_graduates_both_economically_disadvantaged_count': 'ECRB',
    "college_ready_graduates_both_economically_disadvantaged_percent": "{short_code}ECRB{year}R",
    # 'college_ready_graduates_both_limited_english_proficient_count': 'LCRB',
    "college_ready_graduates_both_limited_english_proficient_percent": "{short_code}LCRB{year}R",
    # 'college_ready_graduates_both_at_risk_count': 'RCRB',
    "college_ready_graduates_both_at_risk_percent": "{short_code}RCRB{year}R",
    "avg_sat_score_all_students": "{short_code}A0CSA{year}R",
    "avg_sat_score_african_american": "{short_code}B0CSA{year}R",
    "avg_sat_score_american_indian": "{short_code}I0CSA{year}R",
    "avg_sat_score_asian": "{short_code}30CSA{year}R",
    "avg_sat_score_hispanic": "{short_code}H0CSA{year}R",
    "avg_sat_score_pacific_islander": "{short_code}40CSA{year}R",
    "avg_sat_score_two_or_more_races": "{short_code}20CSA{year}R",
    "avg_sat_score_white": "{short_code}W0CSA{year}R",
    "avg_sat_score_economically_disadvantaged": "{short_code}E0CSA{year}R",
    "avg_act_score_all_students": "{short_code}A0CAA{year}R",
    "avg_act_score_african_american": "{short_code}B0CAA{year}R",
    "avg_act_score_american_indian": "{short_code}I0CAA{year}R",
    "avg_act_score_asian": "{short_code}30CAA{year}R",
    "avg_act_score_hispanic": "{short_code}H0CAA{year}R",
    "avg_act_score_pacific_islander": "{short_code}40CAA{year}R",
    "avg_act_score_two_or_more_races": "{short_code}20CAA{year}R",
    "avg_act_score_white": "{short_code}W0CAA{year}R",
    "avg_act_score_economically_disadvantaged": "{short_code}E0CAA{year}R",
    # 'ap_ib_all_students_count_above_criterion': 'A0BKA',
    "ap_ib_all_students_percent_above_criterion": "{short_code}A0BKA{year}R",
    # 'ap_ib_african_american_count_above_criterion': 'B0BKA',
    "ap_ib_african_american_percent_above_criterion": "{short_code}B0BKA{year}R",
    # 'ap_ib_asian_count_above_criterion': '30BKA',
    "ap_ib_asian_percent_above_criterion": "{short_code}30BKA{year}R",
    # 'ap_ib_hispanic_count_above_criterion': 'H0BKA',
    "ap_ib_hispanic_percent_above_criterion": "{short_code}H0BKA{year}R",
    # 'ap_ib_american_indian_count_above_criterion': 'I0BKA',
    "ap_ib_american_indian_percent_above_criterion": "{short_code}I0BKA{year}R",
    # 'ap_ib_pacific_islander_count_above_criterion': '40BKA',
    "ap_ib_pacific_islander_percent_above_criterion": "{short_code}40BKA{year}R",
    # 'ap_ib_two_or_more_races_count_above_criterion': '20BKA',
    "ap_ib_two_or_more_races_percent_above_criterion": "{short_code}20BKA{year}R",
    # 'ap_ib_white_count_above_criterion': 'W0BKA',
    "ap_ib_white_percent_above_criterion": "{short_code}W0BKA{year}R",
    # 'ap_ib_economically_disadvantaged_count_above_criterion': 'E0BKA',
    "ap_ib_economically_disadvantaged_percent_above_criterion": "{short_code}E0BKA{year}R",
    "ap_ib_all_students_percent_taking": "{short_code}A0BTA{year}R",
    "ap_ib_african_american_percent_taking": "{short_code}B0BTA{year}R",
    "ap_ib_asian_percent_taking": "{short_code}30BTA{year}R",
    "ap_ib_hispanic_percent_taking": "{short_code}H0BTA{year}R",
    "ap_ib_american_indian_percent_taking": "{short_code}I0BTA{year}R",
    "ap_ib_pacific_islander_percent_taking": "{short_code}40BTA{year}R",
    "ap_ib_two_or_more_races_percent_taking": "{short_code}20BTA{year}R",
    "ap_ib_white_percent_taking": "{short_code}W0BTA{year}R",
    "ap_ib_economically_disadvantaged_percent_taking": "{short_code}E0BTA{year}R",
    # # 'dropout_all_students_count': 'A0912DR',
    # 'dropout_all_students_percent': 'A0912DR',
    # # 'dropout_african_american_count': 'B0912DR',
    # 'dropout_african_american_percent': 'B0912DR',
    # # 'dropout_asian_count': '30912DR',
    # 'dropout_asian_percent': '30912DR',
    # # 'dropout_hispanic_count': 'H0912DR',
    # 'dropout_hispanic_percent': 'H0912DR',
    # # 'dropout_american_indian_count': 'I0912DR',
    # 'dropout_american_indian_percent': 'I0912DR',
    # # 'dropout_pacific_islander_count': '40912DR',
    # 'dropout_pacific_islander_percent': '40912DR',
    # # 'dropout_two_or_more_races_count': '20912DR',
    # 'dropout_two_or_more_races_percent': '20912DR',
    # # 'dropout_white_count': 'W0912DR',
    # 'dropout_white_percent': 'W0912DR',
    # # 'dropout_at_risk_count': 'R0912DR',
    # 'dropout_at_risk_percent': 'R0912DR',
    # # 'dropout_economically_disadvantaged_count': 'E0912DR',
    # 'dropout_economically_disadvantaged_percent': 'E0912DR',
    # # 'dropout_limited_english_proficient_count': 'E0912DR',
    # 'dropout_limited_english_proficient_percent': 'E0912DR',
    # # 'four_year_graduate_all_students_count': 'AGC4X',
    # 'four_year_graduate_all_students_percent': 'AGC4X',
    # # 'four_year_graduate_african_american_count': 'BGC4X',
    # 'four_year_graduate_african_american_percent': 'BGC4X',
    # # 'four_year_graduate_american_indian_count': 'IGC4X',
    # 'four_year_graduate_american_indian_percent': 'IGC4X',
    # # 'four_year_graduate_asian_count': '3GC4X',
    # 'four_year_graduate_asian_percent': '3GC4X',
    # # 'four_year_graduate_hispanic_count': 'HGC4X',
    # 'four_year_graduate_hispanic_percent': 'HGC4X',
    # # 'four_year_graduate_pacific_islander_count': '4GC4X',
    # 'four_year_graduate_pacific_islander_percent': '4GC4X',
    # # 'four_year_graduate_two_or_more_races_count': '2GC4X',
    # 'four_year_graduate_two_or_more_races_percent': '2GC4X',
    # # 'four_year_graduate_white_count': 'WGC4X',
    # 'four_year_graduate_white_percent': 'WGC4X',
    # # 'four_year_graduate_at_risk_count': 'RGC4X',
    # 'four_year_graduate_at_risk_percent': 'RGC4X',
    # # 'four_year_graduate_economically_disadvantaged_count': 'EGC4X',
    # 'four_year_graduate_economically_disadvantaged_percent': 'EGC4X',
    # # 'four_year_graduate_limited_english_proficient_count': 'L3C4X',
    # 'four_year_graduate_limited_english_proficient_percent': 'L3C4X',
    # attendence
    "attendance_rate": "{short_code}A0AT{year}R",
    # longitudinal-rate
    # 'dropout_all_students_count': 'A0912DR',
    "dropout_all_students_percent": "{short_code}A0912DR{year}R",
    # 'dropout_african_american_count': 'B0912DR',
    "dropout_african_american_percent": "{short_code}B0912DR{year}R",
    # 'dropout_asian_count': '30912DR',
    "dropout_asian_percent": "{short_code}30912DR{year}R",
    # 'dropout_hispanic_count': 'H0912DR',
    "dropout_hispanic_percent": "{short_code}H0912DR{year}R",
    # 'dropout_american_indian_count': 'I0912DR',
    "dropout_american_indian_percent": "{short_code}I0912DR{year}R",
    # 'dropout_pacific_islander_count': '40912DR',
    "dropout_pacific_islander_percent": "{short_code}40912DR{year}R",
    # 'dropout_two_or_more_races_count': '20912DR',
    "dropout_two_or_more_races_percent": "{short_code}20912DR{year}R",
    # 'dropout_white_count': 'W0912DR',
    "dropout_white_percent": "{short_code}W0912DR{year}R",
    # 'dropout_at_risk_count': 'R0912DR',
    "dropout_at_risk_percent": "{short_code}R0912DR{year}R",
    # 'dropout_economically_disadvantaged_count': 'E0912DR',
    "dropout_economically_disadvantaged_percent": "{short_code}E0912DR{year}R",
    # 'dropout_limited_english_proficient_count': 'E0912DR',
    "dropout_limited_english_proficient_percent": "{short_code}E0912DR{year}R",
    # 'four_year_graduate_all_students_count': 'AGC4X',
    "four_year_graduate_all_students_percent": "{short_code}AGC4{suffix}{year}R",
    # 'four_year_graduate_african_american_count': 'BGC4X',
    "four_year_graduate_african_american_percent": "{short_code}BGC4{suffix}{year}R",
    # 'four_year_graduate_american_indian_count': 'IGC4X',
    "four_year_graduate_american_indian_percent": "{short_code}IGC4{suffix}{year}R",
    # 'four_year_graduate_asian_count': '3GC4X',
    "four_year_graduate_asian_percent": "{short_code}3GC4{suffix}{year}R",
    # 'four_year_graduate_hispanic_count': 'HGC4X',
    "four_year_graduate_hispanic_percent": "{short_code}HGC4{suffix}{year}R",
    # 'four_year_graduate_pacific_islander_count': '4GC4X',
    "four_year_graduate_pacific_islander_percent": "{short_code}4GC4{suffix}{year}R",
    # 'four_year_graduate_two_or_more_races_count': '2GC4X',
    "four_year_graduate_two_or_more_races_percent": "{short_code}2GC4{suffix}{year}R",
    # 'four_year_graduate_white_count': 'WGC4X',
    "four_year_graduate_white_percent": "{short_code}WGC4{suffix}{year}R",
    # 'four_year_graduate_at_risk_count': 'RGC4X',
    "four_year_graduate_at_risk_percent": "{short_code}RGC4{suffix}{year}R",
    # 'four_year_graduate_economically_disadvantaged_count': 'EGC4X',
    "four_year_graduate_economically_disadvantaged_percent": "{short_code}EGC4{suffix}{year}R",
    # 'four_year_graduate_limited_english_proficient_count': 'L3C4X',
    "four_year_graduate_limited_english_proficient_percent": "{short_code}L3C4{suffix}{year}R",
    # reference
    "accountability_rating": "{short_code}_RATING",
    # accountability
    "student_achievement_rating": "{short_code}D1G",
    "school_progress_rating": "{short_code}D2G",
    "closing_the_gaps_rating": "{short_code}D3G",
}