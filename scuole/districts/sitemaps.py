from django.contrib.sitemaps import Sitemap

from scuole.districts.models import District


class DistrictSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5
    protocol = 'https'
    limit = 1000

    def items(self):
        return District.objects.all()
