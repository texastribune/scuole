# -*- coding: utf-8 -*-

import re
import string


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
    print s  # 'Beaumont ISD'
    """
    rx = re.compile('|'.join(map(re.escape, key_dict)))

    def one_xlat(match):
        return key_dict[match.group(0)]

    return rx.sub(one_xlat, text)


def cap_after_dash(text):
    """
    A function to capitalize words preceded by a dash (-).

    Usage:
    from core.utils import cap_after_dash

    replace_str = 'Uplift Education-summit'

    print cap_after_dash(replace_str)
    # 'Uplift Education-Summit'
    """
    return re.sub('-[a-z]', lambda s: s.group(0).upper(), text)


def cap_after_parenthesis(text):
    """
    A function to capitalize words preceded by a opened parenthesis.

    Usage:
    from core.utils import cap_after_parenthesis

    replace_str = 'Richard Milburn Academy (ector County)'

    print cap_after_parenthesis(replace_str)
    # 'Richard Milburn Academy (Ector County)'
    """
    return re.sub('\([a-z]', lambda s: s.group(0).upper(), text)


def acad_to_academy(text):
    """
    A function to change `Acad` to `Academy`. Smartly. Tries to ignore
    instances of `Acad` followed by `emy` or `emies`.

    Usage:
    from core.utils import acad_to_academy

    replace_str = 'Harmony Science Acad (Waco)'

    print acad_to_academy(replace_str)
    # 'Harmony Science Academy (Waco)'
    """
    return re.sub('Acad(?!(emy|emies|emia))', 'Academy', text)


def massage_name(text, key_dict):
    """
    A function to combine all the powers of name cleaning provided in `utils`.
    """
    text = string.capwords(text)
    text = string_replace(text, key_dict)
    text = cap_after_dash(text)
    text = cap_after_parenthesis(text)
    text = acad_to_academy(text)

    return text
