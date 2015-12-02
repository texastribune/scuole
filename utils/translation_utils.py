from django.utils import six
from django.utils.functional import lazy
from django.utils.translation import ugettext as _


def _string_format(string, **kwargs):
    """
    Lazy variant of string formatting, needed for translations that require string
    formatting. Based off implementation of Django's string_concat in translation/__init__.py
    """
    return _(string).format(**kwargs)


string_format = lazy(_string_format, six.text_type)
