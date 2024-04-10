from abc import ABC, abstractmethod

from app.models.common import XID, AreaID, Embedding, ResponseLimit
from app.models.place import PlaceInfo, PlacePrediction


class PlacesRepo(ABC):
    @abstractmethod
    def get_most_similar_places(
        self,
        embedding: Embedding,
        limit: ResponseLimit,
        filter_by_areas: list[AreaID],
    ) -> list[PlacePrediction]:
        return NotImplemented

    @abstractmethod
    def get_place_info(self, xid: XID) -> PlaceInfo:
        return NotImplemented
