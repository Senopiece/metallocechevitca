from pathlib import Path

from fastapi import UploadFile

from app.models.common import ImageID
from app.repos.images_repo import ImagesRepo, ImageToServe


class ImagesMock(ImagesRepo):
    def save_image(self, image: UploadFile) -> ImageID:
        return self.get_random_id()

    def get_image_by_id(self, image_id: ImageID) -> ImageToServe | None:
        return ImageToServe(image_bytes=Path("examples/images/rick.png").read_bytes())
