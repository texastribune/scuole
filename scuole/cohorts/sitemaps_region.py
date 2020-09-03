from django.contrib.sitemaps import Sitemap

from scuole.regions.models import RegionCohorts

class RegionCohortSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return RegionCohorts.objects.all()
