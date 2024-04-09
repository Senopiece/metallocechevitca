from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile

from app.dependencies import get_categories_repo, get_places_repo
from app.models.image_query import ImageQueryRequest, ImageQueryResponse
from app.models.text_query import TextQueryRequest, TextQueryResponse
from app.repos.categories_repo import CategoriesRepo
from app.repos.places_repo import PlacesRepo

router = APIRouter(prefix="/search")


@router.get("/text/", response_model=TextQueryResponse)
async def search_by_text(
    text_query: Annotated[TextQueryRequest, Depends()],
    repo: Annotated[PlacesRepo, Depends(get_places_repo)],
) -> TextQueryResponse:
    # TODO: dependency for embedding?
    return TextQueryResponse(
        places=repo.get_most_similar_places(
            ..., text_query.places_limit, text_query.areas_id
        )
    )


@router.put("/image/", response_model=ImageQueryResponse)
async def search_by_image(
    image_file: UploadFile,
    image_query: Annotated[ImageQueryRequest, Depends()],
    places_repo: Annotated[PlacesRepo, Depends(get_places_repo)],
    categories_repo: Annotated[CategoriesRepo, Depends(get_categories_repo)],
) -> ImageQueryResponse:
    # TODO: dependency for embedding?
    return ImageQueryResponse(
        places=places_repo.get_most_similar_places(
            ..., image_query.places_limit, image_query.areas_id
        ),
        categories=categories_repo.get_most_similar_categories(...),
    )
