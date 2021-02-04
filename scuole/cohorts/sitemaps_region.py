from django.contrib.sitemaps import Sitemap

from scuole.regions.models import Region, RegionCohorts

class RegionCohortSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5
    protocol = 'https'
    limit = 1000

    def items(self):
        return Region.objects.all()

    def location(self, obj):
        from django.urls import reverse
        url = reverse("cohorts:regions", kwargs={"slug": obj.slug})
        return url
