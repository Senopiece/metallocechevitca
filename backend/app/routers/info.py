from typing import Annotated

from fastapi import APIRouter, Depends

from app.models.area import Area
from app.dependencies import get_areas_repo
from app.repos.areas_repo import AreasRepo

router = APIRouter(prefix="/info")


@router.get("/areas/", response_model=list[Area])
async def get_areas(repo: Annotated[AreasRepo, Depends(get_areas_repo)]) -> list[Area]:
    return repo.get_areas()
