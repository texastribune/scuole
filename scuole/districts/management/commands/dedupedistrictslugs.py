from django.core.management.base import BaseCommand
from django.db.models import Count
from django.utils.text import slugify

from scuole.districts.models import District


class Command(BaseCommand):
    help = "Dedupe District slugs by adding the county name to the end."

    def handle(self, *args, **options):
        duplicate_slugs = (
            District.objects.values("slug")
            .annotate(total=Count("slug"))
            .filter(total__gt=1)
        )

        for duplicate in duplicate_slugs:
            slug = duplicate['slug']

            for district in District.objects.filter(slug=slug):
                county_slug = slugify(district.county, allow_unicode=True)
                district_name_slug = slugify(district.name, allow_unicode=True)
                district.slug = f"{district_name_slug}-{county_slug}"
                district.save()


