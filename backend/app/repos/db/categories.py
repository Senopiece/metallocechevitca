from typing import Self

from pymilvus import Collection, CollectionSchema, DataType, FieldSchema, connections
from pymilvus.orm.constants import UNLIMITED

from app.models.category import CategoryInput, CategoryPrediction
from app.models.common import EMB_VECTOR_DIM, Embedding
from app.repos.categories_repo import CategoriesRepo
from app.repos.db.settings import settings


class CategoriesDB(CategoriesRepo):
    EMB_COLLECTION_NAME = "category_emb"
    EMBEDDING_FIELD = "embedding"
    METRIC_TYPE = "COSINE"

    def __init__(self, milvus_uri: str, flush_every_time: bool = False) -> None:
        connections.connect(uri=milvus_uri)
        self.collection: Collection = self._create_emb_collection()
        self.collection.load()
        self.flush_every_time = flush_every_time

    @classmethod
    def from_env(cls) -> Self:
        return cls(
            milvus_uri=str(settings.milvus_uri),
            flush_every_time=settings.flush_every_time,
        )

    def _create_emb_collection(self) -> Collection:
        primary_key = FieldSchema(
            "category", dtype=DataType.VARCHAR, is_primary=True, max_length=128
        )
        embedding = FieldSchema(
            self.EMBEDDING_FIELD, dtype=DataType.FLOAT_VECTOR, dim=EMB_VECTOR_DIM
        )

        schema = CollectionSchema(
            fields=[
                primary_key,
                embedding,
            ]
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

    def get_most_similar_categories(
        self, embedding: Embedding
    ) -> list[CategoryPrediction]:
        result = self.collection.search(
            [embedding],
            self.EMBEDDING_FIELD,
            param={"metric_type": self.METRIC_TYPE},
            output_fields=["category"],
            limit=UNLIMITED,
        )

        return [
            CategoryPrediction(name=hit.get("name"), probability=hit.distance)
            for hit in result
        ]

    def add_category(self, category: CategoryInput) -> bool:
        result = self.collection.insert(category.model_dump(by_alias=True))
        if self.flush_every_time:
            self.collection.flush()
        return result.insert_count > 0