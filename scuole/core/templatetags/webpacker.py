from json import load
from os.path import join

from django import template
from django.conf import settings
from django.utils.html import format_html_join

register = template.Library()


@register.simple_tag
def javascript_pack(entrypoint):
    with open(settings.WEBPACKER_MANIFEST_FILE) as infile:
        manifest = load(infile)

    scripts = manifest[entrypoint]["js"]

    return format_html_join(
        "\n", '<script defer src="{}"></script>', ((join(settings.STATIC_URL, src),) for src in scripts)
    )
