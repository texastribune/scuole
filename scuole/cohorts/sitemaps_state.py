from django.contrib.sitemaps import Sitemap

from scuole.states.models import StateCohorts

class StateCohortSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return StateCohorts.objects.all()
