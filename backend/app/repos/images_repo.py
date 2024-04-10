import uuid
from abc import ABC, abstractmethod
from typing import NamedTuple

from fastapi import UploadFile

from app.models.common import ImageID


class ImageToServe(NamedTuple):
    image_bytes: bytes
    media_type: str = "image/png"


class ImagesRepo(ABC):
    @abstractmethod
    def get_image_by_id(self, image_id: ImageID) -> ImageToServe | None:
        return NotImplemented

    @abstractmethod
    def save_image(self, image: UploadFile) -> ImageID:
        return NotImplemented

    @staticmethod
    def get_random_id() -> ImageID:
        return uuid.uuid4()
