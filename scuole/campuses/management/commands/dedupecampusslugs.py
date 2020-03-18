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

        # loop through all duplicate slugs
        for duplicate in duplicate_slugs:
            slug = duplicate['slug']
            campuses_dup_slug = Campus.objects.filter(slug=slug)

            # if the district and county are the same, but the city of the campuses are different
            if all(obj.district == campuses_dup_slug[0].district for obj in campuses_dup_slug) and all(obj.county == campuses_dup_slug[0].county for obj in campuses_dup_slug):
                for campus in campuses_dup_slug:
                    if campus.city != None:
                        city_slug = slugify(campus.city, allow_unicode=True)
                        campus.slug = f"{campus.slug}-{city_slug}"
                        campus.save()
   
            # if the district, county, and city of the campuses are the same
            if all(obj.district == campuses_dup_slug[0].district for obj in campuses_dup_slug) and all(obj.county == campuses_dup_slug[0].county for obj in campuses_dup_slug) and all(obj.city == campuses_dup_slug[0].city for obj in campuses_dup_slug):
                for campus in campuses_dup_slug:
                    campus.slug = f"{campus.slug}-{campus.tea_id}"
                    campus.save()
