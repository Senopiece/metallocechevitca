from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import image, info, place, search, upload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(info.router)
app.include_router(search.router)
app.include_router(image.router)
app.include_router(place.router)
app.include_router(upload.router)