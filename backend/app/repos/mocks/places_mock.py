from app.models.common import XID, AreaID, Embedding, ImageID, ResponseLimit
from app.models.place import PlaceInfo, PlaceInput, PlacePrediction
from app.repos.places_repo import PlacesRepo


class PlacesMock(PlacesRepo):

    def __init__(self):
        self.XID_TO_INFO: dict[XID, PlaceInfo] = {
            "N555": PlaceInfo(category="памятник", images=["0", "1"]),
            "W123": PlaceInfo(category="музей", images=["2", "3"]),
            "W321": PlaceInfo(category="театр", images=["4", "5"]),
        }

    def add_place_image(self, xid: XID, image_id: ImageID) -> None: ...

    def exists_place(self, xid: XID) -> bool:
        return True

    def upload_place(self, place_data: PlaceInput) -> bool:
        return True

    def get_place_info(self, xid: XID) -> PlaceInfo:
        return self.XID_TO_INFO.get(XID, PlaceInfo(category="mock", images=[0, 1]))

    def get_most_similar_places(
        self, embedding: Embedding, limit: ResponseLimit, filter_by_areas: list[AreaID]
    ) -> list[PlacePrediction]:
        return [
            PlacePrediction(
                xid="N555",
                name="Памятник",
                longitude=0.0,
                latitude=0.0,
                probability=0.9,
                city_id=1,
            ),
            PlacePrediction(
                xid="W123",
                name="Музей",
                longitude=0.0,
                latitude=0.0,
                probability=0.7,
                city_id=1,
            ),
            PlacePrediction(
                xid="W321",
                name="Театр",
                longitude=0.0,
                latitude=0.0,
                probability=0.5,
                city_id=2,
            ),
        ][:limit]
