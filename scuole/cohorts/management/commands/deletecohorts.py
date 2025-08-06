from django.core.management.base import BaseCommand
from scuole.counties.models import CountyCohorts
from scuole.regions.models import RegionCohorts  
from scuole.states.models import StateCohorts


class Command(BaseCommand):
    help = 'Delete all cohorts data'

    def handle(self, *args, **options):
        self.stdout.write("Deleting all cohorts data...")
        
        # Count and delete county cohorts
        county_count = CountyCohorts.objects.count()
        self.stdout.write(f"Deleting {county_count} county cohorts...")
        CountyCohorts.objects.all().delete()
        
        # Count and delete region cohorts  
        region_count = RegionCohorts.objects.count()
        self.stdout.write(f"Deleting {region_count} region cohorts...")
        RegionCohorts.objects.all().delete()
        
        # Count and delete state cohorts
        state_count = StateCohorts.objects.count() 
        self.stdout.write(f"Deleting {state_count} state cohorts...")
        StateCohorts.objects.all().delete()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully deleted all cohorts: {county_count + region_count + state_count} total records'
            )
        )