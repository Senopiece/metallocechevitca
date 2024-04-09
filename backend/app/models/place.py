from pydantic import BaseModel, Field
from app.models.common import NonEmptyString, Probability, XID, Category, ImageID, AreaID


class PlacePrediction(BaseModel):
    xid: XID = Field(alias="XID")
    name: NonEmptyString = Field(alias="Name")
    longitude: float = Field(alias="Lon")
    latitude: float = Field(alias="Lat")
    probability: Probability


class PlaceInfo(BaseModel):
    category: Category
    city_id: AreaID
    images: list[ImageID]

