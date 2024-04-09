from fastapi import Query
from pydantic import BaseModel, Field

from app.models.common import NonEmptyString, QueryRequest
from app.models.place import PlacePrediction


class TextQueryResponse(BaseModel):
    places: list[PlacePrediction]


class TextQueryRequest(QueryRequest):
    query: NonEmptyString = Field(Query(...))
