from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from app.dependencies import get_images_repo
from app.models.common import ImageID
from app.repos.images_repo import ImagesRepo

router = APIRouter(prefix="/image")


@router.get("/{image_id}", response_class=FileResponse)
async def get_image(
    image_id: ImageID, repo: Annotated[ImagesRepo, Depends(get_images_repo)]
) -> FileResponse:
    image_to_serve = repo.get_image_path_by_id(image_id)
    return FileResponse(image_to_serve.path, media_type=image_to_serve.media_type)
