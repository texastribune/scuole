from django.db import models
from django.utils.text import slugify


class Campus(models.Model):
    slug = models.SlugField()
    # CCD fields
    name = models.CharField(help_text="Campus name", max_length=200)
    phone = models.CharField(
        help_text="Campus phone number", max_length=10)
    city = models.CharField(
        help_text="Campus city", max_length=200)
    zip = models.CharField(
        help_text="Campus zip", max_length=5)
    zip4 = models.CharField(
        help_text="Campus +4 zip", max_length=4)
    status = models.CharField(
        help_text="Campus NCES status code", max_length=1)
    locale = models.CharField(
        help_text="Campus NCES urban-centric locale code", max_length=2)
    latitude = models.FloatField(help_text="Campus latitude")
    longitude = models.FloatField(help_text="Campus longitude")
    # TAPR fields
    # C_RATING
    rating = models.CharField(
        help_text="Campus rating", max_length=1)
    # CAMPUS
    campus_id = models.CharField(
        help_text="Campus ID", max_length=10)
    # CFLCHART
    charter = models.CharField(
        help_text="Chartered campus", max_length=1)
    # COUNTY
    county = models.CharField(
        help_text="County number campus is located", max_length=100)
    # DISTRICT
    district = models.CharField(
        help_text="District number campus is located", max_length=100)
    # GRDSPAN
    grade_span = models.CharField(
        help_text="Campus span of grade levels based on enrollment",
        max_length=6)
    # GRDTYPE
    level = models.CharField(
        help_text="Campus type: Elementary, Middle, Senior or Both",
        max_length=1)
    # student breakdown 2014
    # CPETALLC
    all_students = models.IntegerField(
        help_text="Campus total student enrollment")
    # CPETBLAP
    african_american = models.FloatField(
        help_text="Percent of African American students enrolled at campus")
    # CPETHISP
    hispanic = models.FloatField(
        help_text="Percent of Hispanic students enrolled at campus")
    # CPETASIP
    asian = models.FloatField(
        help_text="Percent of Asian students enrolled at campus")
    # CPETINDP
    native_american = models.FloatField(
        help_text="Percent of Native American students enrolled at campus")
    # CPETTWOP
    two_or_more = models.FloatField(
        help_text="Percent of students of two-or-more races enrolled at campus")
    # CPETWHIP
    white = models.FloatField(
        help_text="Percent of white students enrolled at campus")
    # CPETRSKP
    at_risk = models.FloatField(
        help_text="Percent of at-risk students enrolled at campus")
    # CPETBILP
    esl = models.FloatField(
        help_text="Percent of ESL students enrolled at campus")
    # CPETECOP
    econ_disadv = models.FloatField(
        help_text="Percent of economocally disadvantaged students enrolled at campus")
    # CPETSPEP
    special_ed = models.FloatField(
        help_text="Percent of special education students enrolled at campus")
    # Teacher and staff breakdown 2014
    # CPSATOFC
    total_staff = models.FloatField(
        help_text="Total full time staff at campus")
    # CPSSTOSA
    admin_salary = models.FloatField(
        help_text="School admin total base salary average at campus")
    # CPSTTOSA
    teacher_salary = models.FloatField(
        help_text="Teacher full time base salary average at campus")
    # CPST00SA
    beginning_salary = models.FloatField(
        help_text="Teacher beginning base salary average at campus")
    # CPST01SA
    teacher_1_5y_salary = models.FloatField(
        help_text="Teacher 1-5 years experience base salary average at campus")
    # CPST06SA
    teacher_6_10y_salary = models.FloatField(
        help_text="Teacher 6-10 years experience base salary average at campus")
    # CPST11SA
    teacher_11_20y_salary = models.FloatField(
        help_text="Teacher 11-20 years experience base salary average at campus")
    # CPST20SA
    teacher_20y_plus_salary = models.FloatField(
        help_text="Teacher more than 20 years experience base salary average")
    # s
    # CPSTEXPA
    teacher_experience = models.FloatField(
        help_text="Average teacher experience at campus")
    #  CPSTKIDR
    teacher_student_ratio = models.FloatField(
        help_text="Teacher student ratio at campus")

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)[:50]

        super(Campus, self).save(*args, **kwargs)
