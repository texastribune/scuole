from django.contrib.sitemaps import Sitemap

from scuole.states.models import State


class StateSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return State.objects.all()
