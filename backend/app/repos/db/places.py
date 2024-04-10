from typing import Self

from pymilvus import Collection, CollectionSchema, DataType, FieldSchema, connections

from app.models.common import EMB_VECTOR_DIM, XID, AreaID, Embedding, ResponseLimit
from app.models.place import PlaceInfo, PlacePrediction
from app.repos.db.settings import settings
from app.repos.places_repo import PlacesRepo


class PlacesDB(PlacesRepo):
    EMB_COLLECTION_NAME = "place_emb"
    INFO_COLLECTION_NAME = "place_info"
    METRIC_TYPE = "COSINE"
    EMBEDDING_FIELD = "embedding"

    def __init__(self, milvus_uri: str) -> None:
        connections.connect(uri=milvus_uri)
        self.emb_collection: Collection = self._create_emb_collection()
        self.emb_collection.load()

    def _create_emb_collection(self) -> Collection:
        primary_key = FieldSchema(
            "XID", dtype=DataType.VARCHAR, is_primary=True, max_length=128
        )
        embedding = FieldSchema(
            self.EMBEDDING_FIELD, dtype=DataType.FLOAT_VECTOR, dim=EMB_VECTOR_DIM
        )
        city_id = FieldSchema("city_id", dtype=DataType.INT64)
        xid = FieldSchema(name="name", dtype=DataType.VARCHAR, max_length=512)
        lat = FieldSchema(name="lat", dtype=DataType.FLOAT)
        lon = FieldSchema(name="lon", dtype=DataType.FLOAT)
        category = FieldSchema("category", dtype=DataType.VARCHAR, max_length=128)
        images = FieldSchema("images", dtype=DataType.JSON)

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
        return cls(milvus_uri=str(settings.milvus_uri))

    def get_most_similar_places(
        self, embedding: Embedding, limit: ResponseLimit, filter_by_areas: list[AreaID]
    ) -> list[PlacePrediction]:
        result = self.emb_collection.search(
            [embedding],
            self.EMBEDDING_FIELD,
            param={"metric_type": self.METRIC_TYPE},
            limit=limit,
            expr=f"city_id in {filter_by_areas}",
        )

        return [
            PlacePrediction(
                xid=hit.get("XID"),
                name=hit.id,
                probability=hit.distance,
                longitude=hit.get("lon"),
                latitude=hit.get("lat"),
                city_id=hit.get("city_id"),
            )
            for hits in result
            for hit in hits
        ]

    def get_place_info(self, xid: XID) -> PlaceInfo:
        result = self.emb_collection.query(expr=f"XID=='{xid}'")
        if result:
            hit = result[0]
            return PlaceInfo(category=hit.get("category"), images=hit.get("images"))
