from typing import Self

from pymilvus import Collection, CollectionSchema, DataType, FieldSchema, connections

from app.models.category import CategoryInput, CategoryPrediction
from app.models.common import EMB_VECTOR_DIM, Embedding
from app.repos.categories_repo import CategoriesRepo
from app.repos.db.settings import settings


class CategoriesDB(CategoriesRepo):
    def force_flush(self) -> None:
        self.collection.flush()

    EMB_COLLECTION_NAME = "category_emb"
    EMBEDDING_FIELD = "embedding"
    METRIC_TYPE = "COSINE"

    def __init__(self, milvus_uri: str, flush_every_time: bool = False) -> None:
        self.CAT_NAME_EN_TO_RU: dict[str, str] = {
            "religion": "Религиозный объект",
            "other": "Другое",
            "memorial": "Памятник событию",
            "statue": "Памятник личности",
            "experience": "Экспириенс",
        }
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
            limit=max(self.collection.num_entities, 1),
        )

        return [
            CategoryPrediction(
                category=self.CAT_NAME_EN_TO_RU.get(hit.get("category"), "Другое"),
                probability=hit.distance,
            )
            for hits in result
            for hit in hits
        ]

    def add_category(self, category: CategoryInput) -> bool:
        result = self.collection.insert(category.model_dump(by_alias=True))
        if self.flush_every_time:
            self.collection.flush()
        return result.insert_count > 0
