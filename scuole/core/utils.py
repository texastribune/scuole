# -*- coding: utf-8 -*-

import re


def string_replace(text, key_dict):
    """
    A function to convert text in a string to another string if
    it matches any of the keys in the provided pattern dictionary.
    """
    rx = re.compile('|'.join(map(re.escape, key_dict)))

    def one_xlat(match):
        return key_dict[match.group(0)]

    return rx.sub(one_xlat, text)
