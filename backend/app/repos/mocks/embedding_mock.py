import random

from fastapi import UploadFile

from app.models.common import EMB_VECTOR_DIM, Embedding, NonEmptyString
from app.repos.embedding_repo import EmbeddingRepo


class EmbeddingMock(EmbeddingRepo):

    @staticmethod
    def _get_random_vector() -> Embedding:
        return [random.random() for _ in range(EMB_VECTOR_DIM)]

    def get_image_embedding(self, image: UploadFile) -> Embedding:
        return self._get_random_vector()

    def get_text_embedding(self, text_query: NonEmptyString) -> Embedding:
        return self._get_random_vector()
