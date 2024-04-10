from app.repos.areas_repo import AreasRepo
from app.repos.categories_repo import CategoriesRepo
from app.repos.images_repo import ImagesRepo
from app.repos.mocks.areas_mock import AreasMock
from app.repos.mocks.categories_mock import CategoriesMock
from app.repos.mocks.images_mock import ImagesMock
from app.repos.mocks.places_mock import PlacesMock
from app.repos.places_repo import PlacesRepo


def get_areas_repo() -> AreasRepo:
    return AreasMock()


def get_places_repo() -> PlacesRepo:
    return PlacesMock()


def get_categories_repo() -> CategoriesRepo:
    return CategoriesMock()


def get_images_repo() -> ImagesRepo:
    return ImagesMock()
