from django.views.generic import ListView
# from django.shortcuts import render

from scuole.regions.models import Region


class RegionList(ListView):
    model = Region
    template_name = 'pages/region-landing.html'
