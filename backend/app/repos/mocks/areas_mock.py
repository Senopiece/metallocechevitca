from app.models.area import Area, KNOWN_AREAS
from app.repos.areas_repo import AreasRepo


class AreasMock(AreasRepo):
    def get_areas(self) -> list[Area]:
        return KNOWN_AREAS
