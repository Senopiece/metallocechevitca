from fastapi import Query
from pydantic import (
    UUID4,
    BaseModel,
    Field,
    NonNegativeInt,
    PositiveInt,
    confloat,
    conlist,
    constr,
)

EMB_VECTOR_DIM = 512
NonEmptyString = constr(min_length=1, max_length=255)
Probability = confloat(ge=-1, le=1)

# TODO: define better
XID = NonEmptyString
AreaID = NonNegativeInt
Category = NonEmptyString
ImageID = UUID4
ResponseLimit = PositiveInt
Embedding = conlist(float, min_length=EMB_VECTOR_DIM, max_length=EMB_VECTOR_DIM)


class QueryRequest(BaseModel):
    places_limit: ResponseLimit = Field(Query(5))
    areas_id: list[AreaID] = Field(Query(..., alias="areas_id[]"))
