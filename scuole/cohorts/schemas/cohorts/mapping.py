from scuole.regions.models import Region, RegionCohort
from scuole.states.models import State, StateCohort


MAPPING = [
    {
        'folder': 'cohorts',
        'identifier': None,
        'model': State,
        'stats_model': StateCohort,
    }, {
        'folder': 'region',
        'identifier': 'Region Code',
        'model': Region,
        'stats_model': RegionCohort,
    },
]
