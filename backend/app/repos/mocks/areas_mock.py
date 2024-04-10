from app.models.area import KNOWN_AREAS, Area
from app.repos.areas_repo import AreasRepo


class AreasMock(AreasRepo):
    def get_areas(self) -> list[Area]:
        return KNOWN_AREAS
