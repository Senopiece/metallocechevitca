from pydantic import BaseModel

from app.models.common import AreaID, NonEmptyString


class Area(BaseModel):
    id: AreaID
    name: NonEmptyString
