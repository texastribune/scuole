"""scuole URL Configuration

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
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from scuole.regions.views import RegionList

urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name='pages/landing.html'), name='home'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^regions/$', RegionList.as_view(), name='region-landing'),
] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
