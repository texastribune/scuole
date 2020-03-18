from django.core.management.base import BaseCommand
from django.db.models import Count
from django.utils.text import slugify

from scuole.campuses.models import Campus

class Command(BaseCommand):
    help = "Dedupe Campus slugs by adding the county name to the end."

    def handle(self, *args, **options):
        duplicate_slugs = (
            Campus.objects.values("slug")
            .annotate(total=Count("slug"))
            .filter(total__gt=1)
        )

        print('DUPLICATE SLUGS', duplicate_slugs)

        # loop through all duplicate slugs
        for duplicate in duplicate_slugs:
            slug = duplicate['slug']

            # for campus in Campus.objects.filter(slug=slug):
            #     if campus.city != None:
            #       city_slug = slugify(campus.city, allow_unicode=True)
            #       campus.slug = f"{campus.slug}-{city_slug}"
            #       campus.save()

                # city_slug = slugify(campus.city, allow_unicode=True)
                # campus.slug = f"{campus.slug}-{city_slug}"
                # print(slugify(campus.city, allow_unicode=True))
                # print('SLUG', campus.slug)
                # campus.save()
