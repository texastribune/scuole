from scuole.regions.models import Region, RegionStats
from scuole.states.models import State, StateStats


MAPPING = [
    {
        'folder': 'cohorts',
        'identifier': None,
        'model': State,
        'stats_model': StateStats,
    }, {
        'folder': 'region',
        'identifier': 'Region Code',
        'model': Region,
        'stats_model': RegionStats,
    },
]
