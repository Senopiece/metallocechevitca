from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.models.common import ImageID

router = APIRouter(prefix="/image")


@router.get("/{image_id}", response_class=FileResponse)
async def get_image(image_id: ImageID) -> FileResponse:
    return NotImplemented
