from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, UploadFile, status

from app.dependencies import get_categories_repo, get_images_repo, get_places_repo
from app.models.category import CategoryInput
from app.models.common import XID
from app.models.place import PlaceInput
from app.repos.categories_repo import CategoriesRepo
from app.repos.images_repo import ImagesRepo
from app.repos.places_repo import PlacesRepo

router = APIRouter(prefix="/upload")


@router.post("/place", status_code=status.HTTP_201_CREATED)
async def upload_place(
    place_data: PlaceInput, place_repo: Annotated[PlacesRepo, Depends(get_places_repo)]
) -> None:
    if not place_repo.upload_place(place_data):
        raise HTTPException(status.HTTP_409_CONFLICT)


@router.post("/place/{xid}/image", status_code=status.HTTP_201_CREATED)
async def upload_place_image(
    xid: XID,
    image: UploadFile,
    place_repo: Annotated[PlacesRepo, Depends(get_places_repo)],
    image_repo: Annotated[ImagesRepo, Depends(get_images_repo)],
) -> None:
    if not place_repo.exists_place(xid):
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    image_id = image_repo.save_image(image)
    place_repo.add_place_image(xid, image_id)


@router.post("/category", status_code=status.HTTP_201_CREATED)
async def upload_category(
    category_data: CategoryInput,
    category_repo: Annotated[CategoriesRepo, Depends(get_categories_repo)],
) -> None:
    if not category_repo.add_category(category_data):
        raise HTTPException(status.HTTP_409_CONFLICT)
