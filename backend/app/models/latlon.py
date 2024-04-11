from pydantic import BaseModel, Field


class LatLon(BaseModel):
    lon: float = Field(alias="Lon")
    lat: float = Field(alias="Lat")
