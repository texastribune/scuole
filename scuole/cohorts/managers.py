from django.db import models, transaction
from django.db.models import DecimalField, F, FloatField, IntegerField, Value
from django.db.models.functions import Coalesce

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
        return self.overall(**kwargs).order_by('year').first()

    def aggregate_by_year(self, **kwargs):
        output = []

        for obj in self.filter(**kwargs):
            data = {key: getattr(obj, key) for key in year_aggregation_fields}
            output.append({'year': obj.year.start_year, **data})

        return output

    def data_payload(self, year=None):
        model = self.model

        if year:
            economically_disadvantaged = self.by_economic_status(
                model.ECONOMICALLY_DISADVANTAGED).aggregate_by_year(year=year)
            not_economically_disadvantaged = self.by_economic_status(
                model.NOT_ECONOMICALLY_DISADVANTAGED).aggregate_by_year(year=year)
            male = self.by_gender(model.MALE).aggregate_by_year(year=year)
            female = self.by_gender(model.FEMALE).aggregate_by_year(year=year)
            black = self.by_ethnicity(
                model.AFRICAN_AMERICAN).aggregate_by_year(year=year)
            hispanic = self.by_ethnicity(model.HISPANIC).aggregate_by_year(year=year)
            white = self.by_ethnicity(model.WHITE).aggregate_by_year(year=year)
            other = self.by_ethnicity(model.OTHERS).aggregate_by_year(year=year)
            unknown = self.by_ethnicity(model.UNKNOWN).aggregate_by_year(year=year)

            return {
                'economically_disadvantaged': economically_disadvantaged[0] if
                    len(economically_disadvantaged) > 0 else None,
                'not_economically_disadvantaged': not_economically_disadvantaged[0] if
                    len(not_economically_disadvantaged) > 0 else None,
                'male': male[0] if len(male) > 0 else None,
                'female': female[0] if len(female) > 0 else None,
                'black': black[0] if len(black) > 0 else None,
                'hispanic': hispanic[0] if len(hispanic) > 0 else None,
                'white': white[0] if len(white) > 0 else None,
                'other': other[0] if len(other) > 0 else None,
                'unknown': unknown[0] if len(unknown) > 0 else None,
            }
        else:
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
                'unknown': self.by_ethnicity(model.UNKNOWN).aggregate_by_year(),
            }

    def sum_update_or_create(self, defaults=None, **kwargs):
        """
        Look up an object with the given kwargs, summing one with defaults
        if it exists, otherwise create a new one.

        Return a tuple (object, created), where created is a boolean
        specifying whether an object was created.
        """
        defaults = defaults or {}
        params = self._extract_model_params(defaults, **kwargs)

        # we don't want the id that comes over when creating a new object!
        # this id already exists on another object
        # we want the new object to have its own unique id
        defaults.pop('id', None)

        self._for_write = True

        with transaction.atomic(using=self.db):
            try:
                obj = self.select_for_update().get(**kwargs)
            except self.model.DoesNotExist:
                obj, created = self.get_or_create(**kwargs, defaults=defaults)
                if created:
                    return obj, created

            for k, v in defaults.items():
                value = v() if callable(v) else v
                if isinstance(self.model._meta.get_field(k), (
                        DecimalField, FloatField, IntegerField,)):
                    if getattr(obj, k, None) is None and value is not None:
                        setattr(obj, k, value)
                    else:
                        setattr(obj, k, F(k) + (Value(0) if value is None else value))
                else:
                    setattr(obj, k, value)

            obj.save(using=self.db)

        return obj, False
