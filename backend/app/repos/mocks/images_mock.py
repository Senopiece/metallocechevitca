from pathlib import Path

from fastapi import UploadFile

from app.models.common import ImageID
from app.repos.images_repo import ImagesRepo, ImageToServe


class ImagesMock(ImagesRepo):
    def __init__(self):
        self.last_id = 0

    def save_image(self, image: UploadFile) -> ImageID:
        self.last_id += 1
        return self.last_id

    def get_image_path_by_id(self, image_id: ImageID) -> ImageToServe:
        return ImageToServe(path=Path("examples/images/rick.png"))
