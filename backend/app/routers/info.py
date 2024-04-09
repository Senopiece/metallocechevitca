from fastapi import APIRouter

from app.models.area import Area
from app.repos.mocks.areas_mock import AreasMock

router = APIRouter(prefix="/info")


@router.get("/areas/", response_model=list[Area])
async def get_areas() -> list[Area]:
    return AreasMock().get_areas()
