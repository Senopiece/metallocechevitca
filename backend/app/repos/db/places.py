from typing import Any, Self

from pymilvus import Collection, CollectionSchema, DataType, FieldSchema, connections

from app.models.common import (
    EMB_VECTOR_DIM,
    XID,
    AreaID,
    Embedding,
    ImageID,
    ResponseLimit,
)
from app.models.place import PlaceInfo, PlaceInput, PlacePrediction
from app.repos.db.settings import settings
from app.repos.places_repo import PlacesRepo


class PlacesDB(PlacesRepo):
    EMB_COLLECTION_NAME = "place_emb"
    INFO_COLLECTION_NAME = "place_info"
    METRIC_TYPE = "COSINE"
    EMBEDDING_FIELD = "embedding"

    def __init__(self, milvus_uri: str, flush_every_time: bool = False) -> None:
        connections.connect(uri=milvus_uri)
        self.collection: Collection = self._create_emb_collection()
        self.collection.load()
        self.flush_every_time = flush_every_time

    def exists_place(self, xid: XID) -> bool:
        return self._get_by_xid(xid, ["XID"]) is not None

    def _create_emb_collection(self) -> Collection:
        primary_key = FieldSchema(
            "XID", dtype=DataType.VARCHAR, is_primary=True, max_length=128
        )
        embedding = FieldSchema(
            self.EMBEDDING_FIELD, dtype=DataType.FLOAT_VECTOR, dim=EMB_VECTOR_DIM
        )
        city_id = FieldSchema("city_id", dtype=DataType.INT64)
        xid = FieldSchema(name="Name", dtype=DataType.VARCHAR, max_length=512)
        lat = FieldSchema(name="Lat", dtype=DataType.FLOAT)
        lon = FieldSchema(name="Lon", dtype=DataType.FLOAT)
        category = FieldSchema("category", dtype=DataType.VARCHAR, max_length=128)
        images = FieldSchema(
            "images",
            dtype=DataType.ARRAY,
            element_type=DataType.VARCHAR,
            # the maximum number of images per place in dataset is around 130, so 256 seems like sensible upper limit
            max_capacity=256,
            max_length=36,  # length of UUID4
        )

        schema = CollectionSchema(
            fields=[primary_key, embedding, city_id, xid, lat, lon, category, images]
        )
        collection = Collection(name=self.EMB_COLLECTION_NAME, schema=schema)
        collection.create_index(
            self.EMBEDDING_FIELD,
            {
                "index_type": "FLAT",  # maybe use other index?
                "metric_type": self.METRIC_TYPE,
            },
        )
        return collection

    @classmethod
    def from_env(cls) -> Self:
        return cls(
            milvus_uri=str(settings.milvus_uri),
            flush_every_time=settings.flush_every_time,
        )

    def get_most_similar_places(
        self, embedding: Embedding, limit: ResponseLimit, filter_by_areas: list[AreaID]
    ) -> list[PlacePrediction]:
        result = self.collection.search(
            [embedding],
            self.EMBEDDING_FIELD,
            param={"metric_type": self.METRIC_TYPE},
            limit=limit,
            expr=f"city_id in {filter_by_areas}",
            output_fields=["XID", "Name", "Lon", "Lat", "city_id"],
        )

        return [
            PlacePrediction(
                xid=hit.id,
                name=hit.get("Name"),
                probability=hit.distance,
                longitude=hit.get("Lon"),
                latitude=hit.get("Lat"),
                city_id=hit.get("city_id"),
            )
            for hits in result
            for hit in hits
        ]

    def _get_by_xid(
        self, xid: XID, fields: list[str] | None = None
    ) -> dict[str, Any] | None:
        if fields is None:
            fields = ["XID", "category", "images"]
        result = self.collection.query(expr=f"XID=='{xid}'", output_fields=fields)
        if result:
            hit = result[0]
            return hit

    def get_place_info(self, xid: XID) -> PlaceInfo:
        hit = self._get_by_xid(xid)
        if hit is not None:
            return PlaceInfo(category=hit.get("category"), images=hit.get("images"))

    def upload_place(self, place_data: PlaceInput) -> bool:
        result = self.collection.insert(place_data.model_dump(by_alias=True))
        if self.flush_every_time:
            self.collection.flush()
        return result.insert_count > 0

    def add_place_image(self, xid: XID, image_id: ImageID) -> None:
        existing_hit = self._get_by_xid(
            xid,
            [
                "XID",
                "Name",
                self.EMBEDDING_FIELD,
                "city_id",
                "Lat",
                "Lon",
                "category",
                "images",
            ],
        )
        if existing_hit is not None:
            existing_hit["images"] = existing_hit.get("images", []) + [str(image_id)]
            self.collection.upsert(existing_hit)
