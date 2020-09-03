from django.contrib.sitemaps import Sitemap

from scuole.counties.models import CountyCohorts

class CountyCohortSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return CountyCohorts.objects.all()
