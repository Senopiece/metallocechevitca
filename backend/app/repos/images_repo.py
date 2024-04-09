from abc import ABC, abstractmethod

from app.models.common import ImageID


class ImagesRepo(ABC):
    @abstractmethod
    def get_image_by_id(self, image_id: ImageID) -> ...:
        # TODO: decide on return type
        return NotImplemented
