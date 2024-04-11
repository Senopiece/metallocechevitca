import uuid

from app.models.common import XID, AreaID, Embedding, ImageID, ResponseLimit
from app.models.place import PlaceInfo, PlaceInput, PlacePrediction
from app.repos.places_repo import PlacesRepo


class PlacesMock(PlacesRepo):

    def force_flush(self) -> None: ...

    def __init__(self):
        self.XID_TO_INFO: dict[XID, PlaceInfo] = {
            "N555": PlaceInfo(category="памятник", images=[uuid.uuid4(), uuid.uuid4()]),
            "W123": PlaceInfo(category="музей", images=[uuid.uuid4(), uuid.uuid4()]),
            "W321": PlaceInfo(category="театр", images=[uuid.uuid4(), uuid.uuid4()]),
        }

    def add_place_image(self, xid: XID, image_id: ImageID) -> None: ...

    def exists_place(self, xid: XID) -> bool:
        return True

    def upload_place(self, place_data: PlaceInput) -> bool:
        return True

    def get_place_info(self, xid: XID) -> PlaceInfo:
        return self.XID_TO_INFO.get(
            XID, PlaceInfo(category="mock", images=[uuid.uuid4(), uuid.uuid4()])
        )

    def get_most_similar_places(
        self, embedding: Embedding, limit: ResponseLimit, filter_by_areas: list[AreaID]
    ) -> list[PlacePrediction]:
        return [
            PlacePrediction(
                xid="N555",
                name="Памятник",
                longitude=49.144927,
                latitude=55.783582,
                probability=0.9,
                city_id=1,
            ),
            PlacePrediction(
                xid="W123",
                name="Музей",
                longitude=49.143228,
                latitude=55.781126,
                probability=0.7,
                city_id=1,
            ),
            PlacePrediction(
                xid="W321",
                name="Театр",
                longitude=49.136360,
                latitude=55.780790,
                probability=0.5,
                city_id=1,
            ),
        ][:limit]
