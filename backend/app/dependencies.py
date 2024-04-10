from app.main import app
from app.repos.areas_repo import AreasRepo
from app.repos.categories_repo import CategoriesRepo
from app.repos.embedding_repo import EmbeddingRepo
from app.repos.embeddings.client import EmbeddingClient
from app.repos.images_repo import ImagesRepo
from app.repos.mocks.areas_mock import AreasMock
from app.repos.mocks.categories_mock import CategoriesMock
from app.repos.mocks.images_mock import ImagesMock
from app.repos.mocks.places_mock import PlacesMock
from app.repos.places_repo import PlacesRepo
from app.repos.route_optimizer import RouteOptimizer
from app.repos.route_optimizers.manhettan import ManhettanRouteOptimizer


def get_areas_repo() -> AreasRepo:
    return AreasMock()


def get_places_repo() -> PlacesRepo:
    return PlacesMock()


def get_categories_repo() -> CategoriesRepo:
    return CategoriesMock()


def get_images_repo() -> ImagesRepo:
    return ImagesMock()


def get_embedding_repo() -> EmbeddingRepo:
    return EmbeddingMock()


def get_route_optimizer_repo() -> RouteOptimizer:
    return ManhettanRouteOptimizer()
