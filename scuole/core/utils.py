# -*- coding: utf-8 -*-

import re


def string_replace(text, key_dict):
    """
    A function to convert text in a string to another string if
    it matches any of the keys in the provided pattern dictionary.

    Usage:
    from core.utils import string_replace

    KEY_DICT = {
        'Isd': 'ISD',
    }

    s = string_replace('Beaumont Isd', KEY_DICT)
    print s #  'Beaumont ISD'
    """
    rx = re.compile('|'.join(map(re.escape, key_dict)))

    def one_xlat(match):
        return key_dict[match.group(0)]

    return rx.sub(one_xlat, text)
