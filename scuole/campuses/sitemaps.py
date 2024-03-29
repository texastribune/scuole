from django.contrib.sitemaps import Sitemap

from scuole.campuses.models import Campus


class CampusSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5
    protocol = 'https'
    limit = 1000

    def items(self):
        return Campus.objects.select_related('district')
