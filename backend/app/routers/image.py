from io import BytesIO
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse

from app.dependencies import get_images_repo
from app.models.common import ImageID
from app.repos.images_repo import ImagesRepo

router = APIRouter(prefix="/image")


@router.get("/{image_id}", response_class=StreamingResponse)
async def get_image(
    image_id: ImageID, repo: Annotated[ImagesRepo, Depends(get_images_repo)]
) -> StreamingResponse:
    image_to_serve = repo.get_image_by_id(image_id)
    if image_to_serve is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return StreamingResponse(
        BytesIO(image_to_serve.image_bytes), media_type=image_to_serve.media_type
    )
