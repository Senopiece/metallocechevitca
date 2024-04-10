from pydantic import BaseModel, ConfigDict, Field

from app.models.common import (
    XID,
    AreaID,
    Category,
    Embedding,
    ImageID,
    NonEmptyString,
    Probability,
)


class PlaceInput(BaseModel):
    embedding: Embedding
    xid: XID = Field(alias="XID")
    name: NonEmptyString = Field(alias="Name")
    longitude: float = Field(alias="Lon")
    latitude: float = Field(alias="Lat")
    category: Category
    city_id: AreaID
    images: list[ImageID] = []


class PlacePrediction(BaseModel):
    xid: XID = Field(alias="XID")
    name: NonEmptyString = Field(alias="Name")
    longitude: float = Field(alias="Lon")
    latitude: float = Field(alias="Lat")
    probability: Probability
    city_id: AreaID

    model_config = ConfigDict(populate_by_name=True)


class PlaceInfo(BaseModel):
    category: Category
    images: list[ImageID]
