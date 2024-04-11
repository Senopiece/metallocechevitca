import httpx
from fastapi import UploadFile

from app.models.common import Embedding, NonEmptyString
from app.repos.embedding_repo import EmbeddingRepo


class EmbeddingClient(EmbeddingRepo):
    async def get_image_embedding(self, image: UploadFile) -> Embedding:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8080/image-embedding",
                files={"image": image.file},
            )
            response.raise_for_status()
            return Embedding(response.json()["embedding"])

    async def get_text_embedding(self, text_query: NonEmptyString) -> Embedding:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8080/text-embedding",
                json={"text_query": text_query},
            )
            response.raise_for_status()
            return Embedding(response.json()["embedding"])
