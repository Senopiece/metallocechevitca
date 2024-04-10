from pydantic import BaseModel, Field

class LatLon(BaseModel):
    longitude: float = Field(alias="Lon")
    latitude: float = Field(alias="Lat")
