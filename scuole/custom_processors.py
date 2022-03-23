from scuole.campuses.models import Campus
from scuole.districts.models import District

def district_campus_count(request):
    return {
        'district_count': District.objects.count(),
        'campus_count': Campus.objects.count()
    }
  