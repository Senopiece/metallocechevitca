from abc import ABC, abstractmethod

from app.models.common import ImageID


class ImagesRepo(ABC):
    @abstractmethod
    def get_image_by_id(self, image_id: ImageID) -> ...:
        return NotImplemented
