from typing import Self

from fastapi import UploadFile
from minio import Minio

from app.models.common import ImageID
from app.repos.file_storage.settings import MinIOSettings
from app.repos.images_repo import ImagesRepo, ImageToServe


class ImagesStorage(ImagesRepo):
    def __init__(
        self, endpoint: str, access_key: str, secret_key: str, bucket_name: str
    ):
        self.minio_client = Minio(endpoint, access_key, secret_key)
        self.bucket_name = bucket_name

    @classmethod
    def from_env(cls, settings: MinIOSettings) -> Self:
        return cls(**settings.model_dump())

    def get_image_by_id(self, image_id: ImageID) -> ImageToServe | None:
        result = None
        try:
            response = self.minio_client.get_object(self.bucket_name, image_id)
            result = ImageToServe(response.read(), response.headers.get("content-type"))
        finally:
            response.close()
            response.release_conn()
            return result

    def save_image(self, image: UploadFile) -> ImageID:
        image_id = self.get_random_id()
        self.minio_client.put_object(
            bucket_name=self.bucket_name,
            object_name=image_id,
            data=image.file,
            length=image.size,
            content_type=image.content_type,
        )
        return image_id
