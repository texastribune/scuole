from django.db.models import Func


class Simplify(Func):
    function = 'ST_Simplify'
