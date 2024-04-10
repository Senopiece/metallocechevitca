from fastapi import UploadFile

from app.models.common import EMB_VECTOR_DIM, Embedding, NonEmptyString
from app.repos.embedding_repo import EmbeddingRepo


class EmbeddingMock(EmbeddingRepo):
    def get_image_embedding(self, image: UploadFile) -> Embedding:
        return [0] * EMB_VECTOR_DIM

    def get_text_embedding(self, text_query: NonEmptyString) -> Embedding:
        return [0] * EMB_VECTOR_DIM
