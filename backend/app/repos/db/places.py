from typing import Annotated, Self

from fastapi import Depends
from pymilvus import MilvusClient

from app.models.common import XID, AreaID, Embedding, ResponseLimit
from app.models.place import PlaceInfo, PlacePrediction
from app.repos.db.settings import settings
from app.repos.places_repo import PlacesRepo


class PlacesDB(PlacesRepo):
    def __init__(self, milvus_uri: str) -> None:
        self.client = MilvusClient(milvus_uri)

    @classmethod
    def from_env(cls) -> Self:
        return cls(milvus_uri=str(settings.milvus_uri))

    def get_most_similar_places(
        self, embedding: Embedding, limit: ResponseLimit, filter_by_areas: list[AreaID]
    ) -> list[PlacePrediction]:
        # TODO
        return NotImplemented

    def get_place_info(self, xid: XID) -> PlaceInfo:
        # TODO
        return NotImplemented
