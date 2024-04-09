from fastapi import APIRouter

from app.models.area import Area

router = APIRouter(prefix="/info")


@router.get("/areas/", response_model=list[Area])
async def get_areas() -> list[Area]:
    return NotImplemented
