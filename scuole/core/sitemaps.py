from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5
    protocol = 'https'
    limit = 1000

    def items(self):
            return ['landing', 'about']

    def location(self, item):
        return reverse(item)
