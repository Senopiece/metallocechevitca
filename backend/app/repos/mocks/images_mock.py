from pathlib import Path

from app.models.common import ImageID
from app.repos.images_repo import ImagesRepo, ImageToServe


class ImagesMock(ImagesRepo):
    def get_image_path_by_id(self, image_id: ImageID) -> ImageToServe:
        return ImageToServe(path=Path("examples/images/rick.png"))
