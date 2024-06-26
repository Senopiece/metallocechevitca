from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.repos.db.categories import CategoriesDB
from app.repos.db.places import PlacesDB
from app.repos.file_storage.images import ImagesStorage

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def inject_repos() -> None:
    from app.routers import image, info, place, search, upload

    app.include_router(info.router)
    app.include_router(search.router)
    app.include_router(image.router)
    app.include_router(place.router)
    app.include_router(upload.router)

    app.places_repo = PlacesDB.from_env()
    app.categories_repo = CategoriesDB.from_env()
    app.images_repo = ImagesStorage.from_env()
