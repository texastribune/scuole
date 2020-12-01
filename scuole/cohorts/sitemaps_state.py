from django.contrib.sitemaps import Sitemap

from scuole.states.models import State, StateCohorts

class StateCohortSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5
    protocol = 'https'

    def items(self):
        return State.objects.all()

    def location(self, obj):
        from django.urls import reverse
        url = reverse("cohorts:states", kwargs={"slug": obj.slug})
        return url
