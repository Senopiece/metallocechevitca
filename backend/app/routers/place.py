from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_places_repo
from app.models.common import XID
from app.models.place import PlaceInfo
from app.repos.places_repo import PlacesRepo

router = APIRouter(prefix="/place")


@router.get("/{xid}", response_model=PlaceInfo)
async def get_place_info(
    xid: XID, repo: Annotated[PlacesRepo, Depends(get_places_repo)]
) -> PlaceInfo:
    result = repo.get_place_info(xid)
    if result is not None:
        return result
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
