from django.db import models, transaction
from django.db.models import DecimalField, F, FloatField, IntegerField


class CohortQuerySet(models.QuerySet):
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
