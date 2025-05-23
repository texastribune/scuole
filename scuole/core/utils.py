# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from collections import OrderedDict
import json
import re
import string

from django.contrib.gis.db.models import Extent
from django.urls import reverse

from .functions import Simplify


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
    rx = re.compile("|".join(map(re.escape, key_dict)))

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
    return re.sub("-[a-z]", lambda s: s.group(0).upper(), text)


def cap_after_parenthesis(text):
    """
    A function to capitalize words preceded by a opened parenthesis.

    Usage:
    from core.utils import cap_after_parenthesis

    replace_str = 'Richard Milburn Academy (ector County)'

    print cap_after_parenthesis(replace_str)
    # 'Richard Milburn Academy (Ector County)'
    """
    return re.sub(r"\([a-z]", lambda s: s.group(0).upper(), text)


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
    return re.sub("Acad(?!(emy|emies|emia))", "Academy", text)


def cap_following_o_apostrophe(text):
    """
    A function to capitalize letters that follow `O'`.

    Usage:
    from core.utils import cap_following_o_apostrophe

    replace_str = "O'donnell ISD"

    print cap_following_o_apostrophe(replace_str)
    # "O'Donnell ISD"
    """
    return re.sub(r"O'[a-z]", lambda x: x.group(0).upper(), text)


def remove_charter_c(text):
    """
    A function to remove (C) from charter school names.
    """
    return re.sub(r" \(C\)", "", text)


def massage_name(text, key_dict):
    """
    A function to combine all the powers of name cleaning provided in `utils`.
    """
    text = string.capwords(text)
    text = string_replace(text, key_dict)
    text = cap_after_dash(text)
    text = cap_after_parenthesis(text)
    text = acad_to_academy(text)
    text = cap_following_o_apostrophe(text)

    return text

# def diagnose_gis_imports():
#     """Temporary function to diagnose available GIS imports"""
#     import django
#     print(f"Django version: {django.__version__}")
    
#     # Check what's in the gis module
#     import django.contrib.gis.db.models as gis_models
#     print("Available in django.contrib.gis.db.models:")
#     print([name for name in dir(gis_models) if not name.startswith('_')])
    
#     # Check what's in the functions module
#     import django.contrib.gis.db.models.functions as functions
#     print("\nAvailable in django.contrib.gis.db.models.functions:")
#     print([name for name in dir(functions) if not name.startswith('_')])
    
#     # Check if there's an aggregates module
#     try:
#         import django.contrib.gis.db as db
#         print("\nModules in django.contrib.gis.db:")
#         print([name for name in dir(db) if not name.startswith('_')])
#     except ImportError:
#         print("No access to django.contrib.gis.db")

# # Call the function
# diagnose_gis_imports()

# from django.contrib.gis.db.models import Extent
# from django.contrib.gis.db.models.functions import Simplify

# def build_geojson(queryset, shape_field, fields=None):
#     if fields is None:
#         fields = []
#     output = {"type": "FeatureCollection", "features": []}

#     instances = queryset.annotate(simple_shape=Simplify(shape_field, 0.01))
    
#     # Try without specifying output_field
#     extent = instances.aggregate(extent=Extent("simple_shape"))

#     output["bbox"] = extent["extent"]

#     for instance in instances:
#         shape = json.loads(instance.simple_shape.geojson)
#         fields = {f: getattr(instance, f, None) for f in fields}
#         fields["url"] = reverse("cohorts:regions", kwargs={"slug": instance.slug})

#         output["features"].append(
#             {"type": "Feature", "geometry": shape, "properties": fields}
#         )

#     return output

# this version broke on update to django 3.2.24
# def build_geojson(queryset, shape_field, fields=[]):
#     output = {"type": "FeatureCollection", "features": []}

#     instances = queryset.annotate(simple_shape=Simplify(shape_field, 0.01))
#     extent = instances.aggregate(extent=Extent("simple_shape"))

#     output["bbox"] = extent["extent"]

#     for instance in instances:
#         shape = json.loads(instance.simple_shape.geojson)
#         fields = {f: getattr(instance, f, None) for f in fields}
#         fields["url"] = reverse("cohorts:regions", kwargs={"slug": instance.slug})

#         output["features"].append(
#             {"type": "Feature", "geometry": shape, "properties": fields}
#         )

#     return output

# had to rewrite this code on update to django 3.2.24 (4/3/25)
def build_geojson(queryset, shape_field, fields=None):
    if fields is None:
        fields = []
    output = {"type": "FeatureCollection", "features": []}

    # Skip the simplification temporarily
    instances = queryset
    
    # Skip the extent calculation temporarily
    # We'll add a manual bounding box calculation later if needed
    output["bbox"] = None  # Placeholder
    
    features = []
    for instance in instances:
        shape_value = getattr(instance, shape_field)
        if shape_value:
            shape = json.loads(shape_value.geojson)
            fields_data = {f: getattr(instance, f, None) for f in fields}
            fields_data["url"] = reverse("cohorts:regions", kwargs={"slug": instance.slug})
            
            features.append({
                "type": "Feature", 
                "geometry": shape, 
                "properties": fields_data
            })
    
    output["features"] = features
    return output


def to_geometry(geo_value):
    if geo_value is None:
        return geo_value

    geojson = OrderedDict(json.loads(geo_value.geojson))

    return geojson


def get_properties(instance, fields):
    properties = OrderedDict()

    for field in fields:
        value = getattr(instance, field)

        if callable(value):
            value = value()

        properties[field] = value

    return properties


def to_geojson_feature(instance, geo_field, fields, include_bbox=True, simplify=0.01):
    feature = OrderedDict()

    # GeoJSON spec requires a type of "Feature"
    feature["type"] = "Feature"

    # pull out the GEOSGeometry
    geo_value = getattr(instance, geo_field)

    if geo_value and simplify:
        geo_value = geo_value.simplify(simplify, preserve_topology=True)

    # prepare "geometry" attribute
    feature["geometry"] = to_geometry(geo_value)

    if geo_value and include_bbox:
        feature["bbox"] = geo_value.extent

    feature["properties"] = get_properties(instance, fields)

    return feature

def nameFormat(txt):
    # Takes out MRS, MR, DR, MS with a space after
    return re.sub(r'MRS |MR |DR |MS ', r'', txt)

def addComma(txt):
    # Looks for three spaces to add a comma after a name
    return re.sub(r'   ', r', ', txt)