from app.models.category import CategoryPrediction
from app.models.common import QueryRequest
from app.models.text_query import TextQueryResponse


class ImageQueryResponse(TextQueryResponse):
    categories: list[CategoryPrediction]


class ImageQueryRequest(QueryRequest): ...
