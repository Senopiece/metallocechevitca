from app.models.area import Area
from app.repos.areas_repo import AreasRepo


class AreasMock(AreasRepo):
    def get_areas(self) -> list[Area]:
        return [
            Area(name="Нижний Новгород", id=1),
            Area(name="Екатеринбург", id=2),
        ]
