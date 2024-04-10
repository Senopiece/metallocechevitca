from abc import ABC, abstractmethod
from pathlib import Path
from typing import NamedTuple

from app.models.common import ImageID


class ImageToServe(NamedTuple):
    path: Path
    media_type: str = "image/png"


class ImagesRepo(ABC):
    @abstractmethod
    def get_image_path_by_id(self, image_id: ImageID) -> ImageToServe:
        return NotImplemented
