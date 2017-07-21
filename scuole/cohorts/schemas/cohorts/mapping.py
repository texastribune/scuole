from scuole.regions.models import Region, RegionCohorts
from scuole.states.models import State, StateCohorts


MAPPING = [
    {
        'folder': 'state',
        'identifier': None,
        'model': State,
        'cohorts_model': StateCohorts,
    }, {
        'folder': 'region',
        'identifier': 'Region Code',
        'model': Region,
        'cohorts_model': RegionCohorts,
    },
]
