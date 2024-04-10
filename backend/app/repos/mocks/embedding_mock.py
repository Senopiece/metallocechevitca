from fastapi import UploadFile

from app.models.common import Embedding, NonEmptyString
from app.repos.embedding_repo import EmbeddingRepo


class EmbeddingMock(EmbeddingRepo):
    # TODO
    def get_image_embedding(self, image: UploadFile) -> Embedding:
        return None

    def get_text_embedding(self, text_query: NonEmptyString) -> Embedding:
        return None
