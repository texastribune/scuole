from django.contrib.sitemaps import Sitemap

from scuole.counties.models import County, CountyCohorts

class CountyCohortSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5
    protocol = 'https'

    def items(self):
        return County.objects.all()

    def location(self, obj):
        from django.urls import reverse
        url = reverse("cohorts:counties", kwargs={"slug": obj.slug})
        return url
