from abc import ABC, abstractmethod

from fastapi import UploadFile

from app.models.common import Embedding, NonEmptyString


class EmbeddingRepo(ABC):
    @abstractmethod
    async def get_image_embedding(self, image: UploadFile) -> Embedding:
        return NotImplemented

    @abstractmethod
    async def get_text_embedding(self, text_query: NonEmptyString) -> Embedding:
        return NotImplemented
