from ast import Dict
from collections import defaultdict
from email.policy import default
from typing import Annotated, List

from fastapi import APIRouter, Depends, UploadFile

from app.dependencies import (
    get_categories_repo,
    get_embedding_repo,
    get_places_repo,
    get_route_optimizer_repo,
)
from app.models.image_query import ImageQueryRequest, ImageQueryResponse
from app.models.latlon import LatLon
from app.models.place import PlacePrediction
from app.models.text_query import TextQueryRequest, TextQueryResponse
from app.repos.categories_repo import CategoriesRepo
from app.repos.embedding_repo import EmbeddingRepo
from app.repos.places_repo import PlacesRepo
from app.repos.route_optimizer import RouteOptimizer

router = APIRouter(prefix="/search")


async def optimal_route_for_cities(
    route_optimizer: RouteOptimizer, places: List[PlacePrediction]
):
    # split by cities
    c2ps = defaultdict(lambda: [])
    for place in places:
        c2ps[place.city_id].append(LatLon(Lat=place.latitude, Lon=place.longitude))

    # for each city try to find optimal path and return first found
    for path in c2ps.values():
        optimal_route = await route_optimizer.get_route(path)

        if optimal_route is not None:
            return optimal_route

    # All cities have no feasible route
    return None


@router.get("/text/", response_model=TextQueryResponse)
async def search_by_text(
    text_query: Annotated[TextQueryRequest, Depends()],
    places_repo: Annotated[PlacesRepo, Depends(get_places_repo)],
    embedding_repo: Annotated[EmbeddingRepo, Depends(get_embedding_repo)],
    route_optimizer: Annotated[RouteOptimizer, Depends(get_route_optimizer_repo)],
) -> TextQueryResponse:
    text_emb = await embedding_repo.get_text_embedding(text_query.query)
    places = places_repo.get_most_similar_places(
        text_emb, text_query.places_limit, text_query.areas_id
    )
    return TextQueryResponse(
        places=places,
        optimal_route=await optimal_route_for_cities(route_optimizer, places),
    )


@router.put("/image/", response_model=ImageQueryResponse)
async def search_by_image(
    image_file: UploadFile,
    image_query: Annotated[ImageQueryRequest, Depends()],
    places_repo: Annotated[PlacesRepo, Depends(get_places_repo)],
    categories_repo: Annotated[CategoriesRepo, Depends(get_categories_repo)],
    embedding_repo: Annotated[EmbeddingRepo, Depends(get_embedding_repo)],
    route_optimizer: Annotated[RouteOptimizer, Depends(get_route_optimizer_repo)],
) -> ImageQueryResponse:
    image_emb = await embedding_repo.get_image_embedding(image_file)
    places = places_repo.get_most_similar_places(
        image_emb, image_query.places_limit, image_query.areas_id
    )
    return ImageQueryResponse(
        places=places,
        optimal_route=await optimal_route_for_cities(route_optimizer, places),
        categories=categories_repo.get_most_similar_categories(image_emb),
    )
