from pydantic import BaseModel

from app.models.common import AreaID, NonEmptyString


class Area(BaseModel):
    id: AreaID
    name: NonEmptyString


KNOWN_AREAS = [
    Area(id=1, name="Нижний Новгород"),
    Area(id=2, name="Ярославль"),
    Area(id=3, name="Владимир"),
    Area(id=4, name="Екатеринбург"),
    Area(id=5, name="Воронеж"),
]
