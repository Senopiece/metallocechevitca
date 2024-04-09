from fastapi import APIRouter

from app.models.common import XID
from app.models.place import PlaceInfo

router = APIRouter(prefix="/place")


@router.get("/{xid}", response_model=PlaceInfo)
async def get_place_info(xid: XID) -> PlaceInfo:
    return NotImplemented
