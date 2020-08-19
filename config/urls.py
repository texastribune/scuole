# -*- coding: utf-8 -*-
"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views import defaults as default_views

from scuole.campuses.sitemaps import CampusSitemap
from scuole.core.sitemaps import StaticSitemap
from scuole.core.views import (
    AboutView,
    AcceptRedirectView,
    LandingView,
    LookupView,
    SearchView,
)
from scuole.districts.sitemaps import DistrictSitemap
from scuole.states.sitemaps import StateSitemap

sitemaps = {
    "scuole.campuses": CampusSitemap,
    "scuole.districts": DistrictSitemap,
    "scuole.states": StateSitemap,
    "scuole.core": StaticSitemap,
}

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    path("", LandingView.as_view(), name="landing"),
    path("outcomes/", include("scuole.cohorts.urls", namespace="cohorts")),
    path("districts/", include("scuole.districts.urls", namespace="districts")),
    path("states/", include("scuole.states.urls", namespace="states")),
    path("search/", SearchView.as_view(), name="search"),
    path("lookup/", LookupView.as_view(), name="lookup"),
    path("about/", AboutView.as_view(), name="about"),
    path("redirect/", AcceptRedirectView.as_view(), name="redirect"),
    path("admin/", admin.site.urls),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

# Test pages normally not reachable when DEBUG = True
if settings.DEBUG:
    urlpatterns += [
        path(
            "400/", default_views.bad_request, {"exception": Exception("Bad request")}
        ),
        path(
            "403/",
            default_views.permission_denied,
            {"exception": Exception("Permission denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            {"exception": Exception("Page not found")},
        ),
        path("500/", default_views.server_error),
    ]

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            re_path(r"^__debug__/", include(debug_toolbar.urls))
        ] + urlpatterns
