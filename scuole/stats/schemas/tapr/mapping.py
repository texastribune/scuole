from scuole.campuses.models import Campus, CampusStats
from scuole.districts.models import District, DistrictStats
from scuole.regions.models import Region, RegionStats
from scuole.states.models import State, StateStats

MAPPING = [
    # {
    #     "folder": "state",
    #     "identifier": None,
    #     "id_field": None,
    #     "short_code": "S",
    #     "model": State,
    #     "stats_model": StateStats,
    # },
    # {
    #     "folder": "region",
    #     "identifier": "REGION",
    #     "id_field": "region_id",
    #     "short_code": "R",
    #     "model": Region,
    #     "stats_model": RegionStats,
    # },
    # {
    #     "folder": "district",
    #     "identifier": "DISTRICT",
    #     "id_field": "tea_id",
    #     "short_code": "D",
    #     "model": District,
    #     "stats_model": DistrictStats,
    # },
    {
        "folder": "campus",
        "identifier": "CAMPUS",
        "id_field": "tea_id",
        "short_code": "C",
        "model": Campus,
        "stats_model": CampusStats,
    },
]
