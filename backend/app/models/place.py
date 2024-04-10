from pydantic import BaseModel, ConfigDict, Field

from app.models.common import (
    XID,
    AreaID,
    Category,
    ImageID,
    NonEmptyString,
    Probability,
)


class PlacePrediction(BaseModel):
    xid: XID = Field(alias="XID")
    name: NonEmptyString = Field(alias="Name")
    longitude: float = Field(alias="Lon")
    latitude: float = Field(alias="Lat")
    probability: Probability

    model_config = ConfigDict(populate_by_name=True)


class PlaceInfo(BaseModel):
    category: Category
    city_id: AreaID
    images: list[ImageID]
