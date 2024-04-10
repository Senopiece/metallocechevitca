from abc import ABC, abstractmethod

from app.models.common import XID, AreaID, Embedding, ImageID, ResponseLimit
from app.models.place import PlaceInfo, PlaceInput, PlacePrediction


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
    def exists_place(self, xid: XID) -> bool:
        return NotImplemented

    @abstractmethod
    def get_place_info(self, xid: XID) -> PlaceInfo:
        return NotImplemented

    @abstractmethod
    def upload_place(self, place_data: PlaceInput) -> bool: ...

    @abstractmethod
    def add_place_image(self, xid: XID, image_id: ImageID) -> None: ...
