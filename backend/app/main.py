from fastapi import FastAPI

from app.routers import info, search, image, place

app = FastAPI()

app.include_router(info.router)
app.include_router(search.router)
app.include_router(image.router)
app.include_router(place.router)
