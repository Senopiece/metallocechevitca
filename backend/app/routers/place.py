from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependencies import get_places_repo
from app.models.common import XID
from app.models.place import PlaceInfo
from app.repos.places_repo import PlacesRepo

router = APIRouter(prefix="/place")


@router.get("/{xid}", response_model=PlaceInfo)
async def get_place_info(
    xid: XID, repo: Annotated[PlacesRepo, Depends(get_places_repo)]
) -> PlaceInfo:
    return repo.get_place_info(xid)
