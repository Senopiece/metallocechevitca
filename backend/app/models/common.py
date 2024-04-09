from fastapi import Query
from pydantic import BaseModel, Field, NonNegativeInt, PositiveInt, confloat, constr

NonEmptyString = constr(min_length=1, max_length=255)
Probability = confloat(ge=0, le=1)

# TODO: define better
XID = NonEmptyString
AreaID = NonNegativeInt
Category = NonEmptyString
ImageID = NonNegativeInt
ResponseLimit = PositiveInt
Embedding = ...


class QueryRequest(BaseModel):
    places_limit: ResponseLimit = Field(Query(5))
    areas_id: list[AreaID] = Field(Query(...))
