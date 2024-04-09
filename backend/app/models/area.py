from pydantic import BaseModel

from app.models.common import NonEmptyString, AreaID


class Area(BaseModel):
    id: AreaID
    name: NonEmptyString
