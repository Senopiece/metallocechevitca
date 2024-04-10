from typing import Self

import httpx
from fastapi import UploadFile

from app.models.common import Embedding, NonEmptyString
from app.repos.embedding_repo import EmbeddingRepo
from app.repos.embeddings.settings import ClientSettings


class EmbeddingClient(EmbeddingRepo):
    def __init__(self, url: str) -> None:
        self.url = url

    @classmethod
    def from_env(cls, settings: ClientSettings) -> Self:
        return cls(url=str(settings.url))

    async def get_image_embedding(self, image: UploadFile) -> Embedding:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.url + "/image-embedding",
                files={"image": image.file},
            )
            response.raise_for_status()
            return Embedding(response.json()["embedding"])

    async def get_text_embedding(self, text_query: NonEmptyString) -> Embedding:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.url + "/text-embedding",
                json={"text_query": text_query},
            )
            response.raise_for_status()
            return Embedding(response.json()["embedding"])
