from fastapi import Query
from pydantic import constr, confloat, BaseModel, PositiveInt, NonNegativeInt, Field

NonEmptyString = constr(min_length=1, max_length=255)
Probability = confloat(ge=0, le=1)

# TODO: define better
XID = NonEmptyString
AreaID = NonNegativeInt
Category = NonEmptyString
ImageID = NonNegativeInt
ResponseLimit = PositiveInt


class QueryRequest(BaseModel):
    places_limit: ResponseLimit = Field(Query(5))
    areas_id: list[AreaID] = Field(Query(...))