from abc import ABC, abstractmethod

from app.models.common import ResponseLimit, XID, Embedding
from app.models.place import PlacePrediction, PlaceInfo


class PlacesRepo(ABC):
    @abstractmethod
    def get_most_similar_to(self, embedding: Embedding, limit: ResponseLimit) -> list[PlacePrediction]:
        return NotImplemented

    @abstractmethod
    def get_place_info(self, xid: XID) -> PlaceInfo:
        return NotImplemented
