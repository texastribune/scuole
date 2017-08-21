from django.db import models, transaction
from django.db.models import DecimalField, F, FloatField, IntegerField

year_aggregation_fields = [
    'enrolled_8th',
    'graduated',
    'total_enrolled',
    'total_degrees',
    'percent_graduated',
    'percent_completed_higher_education',
    'percent_enrolled_higher_education',
]


class CohortQuerySet(models.QuerySet):
    def overall(self, **kwargs):
        return self.filter(
            economic_status='', ethnicity='', gender='', **kwargs)

    def by_economic_status(self, economic_status, **kwargs):
        return self.filter(
            ethnicity='', gender='', economic_status=economic_status, **kwargs)

    def by_ethnicity(self, ethnicity, **kwargs):
        return self.filter(
            economic_status='', gender='', ethnicity=ethnicity, **kwargs)

    def by_gender(self, gender, **kwargs):
        return self.filter(
            economic_status='', ethnicity='', gender=gender, **kwargs)

    def latest_cohort(self, **kwargs):
        return self.overall(**kwargs).last()

    def aggregate_by_year(self, **kwargs):
        output = []

        for obj in self:
            data = {key: getattr(obj, key) for key in year_aggregation_fields}
            output.append({'year': obj.year.start_year, **data})

        return output

    def data_payload(self):
        model = self.model

        return {
            'economically_disadvantaged': self.by_economic_status(
                model.ECONOMICALLY_DISADVANTAGED).aggregate_by_year(),
            'not_economically_disadvantaged': self.by_economic_status(
                model.NOT_ECONOMICALLY_DISADVANTAGED).aggregate_by_year(),
            'male': self.by_gender(model.MALE).aggregate_by_year(),
            'female': self.by_gender(model.FEMALE).aggregate_by_year(),
            'black': self.by_ethnicity(
                model.AFRICAN_AMERICAN).aggregate_by_year(),
            'hispanic': self.by_ethnicity(model.HISPANIC).aggregate_by_year(),
            'white': self.by_ethnicity(model.WHITE).aggregate_by_year(),
            'other': self.by_ethnicity(model.OTHERS).aggregate_by_year(),
        }


    def sum_update_or_create(self, defaults=None, **kwargs):
        """
        Look up an object with the given kwargs, summing one with defaults
        if it exists, otherwise create a new one.

        Return a tuple (object, created), where created is a boolean
        specifying whether an object was created.
        """
        defaults = defaults or {}
        lookup, params = self._extract_model_params(defaults, **kwargs)
        self._for_write = True
        with transaction.atomic(using=self.db):
            try:
                obj = self.select_for_update().get(**lookup)
            except self.model.DoesNotExist:
                obj, created = self._create_object_from_params(lookup, params)
                if created:
                    return obj, created
            for k, v in defaults.items():
                if isinstance(self.model._meta.get_field(k), (
                        DecimalField, FloatField, IntegerField,)):
                    setattr(obj, k, F(k) + (v() if callable(v) else v))
                else:
                    setattr(obj, k, v() if callable(v) else v)
            obj.save(using=self.db)
        return obj, False
