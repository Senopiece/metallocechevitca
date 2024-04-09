from typing import Annotated

from fastapi import APIRouter, UploadFile, Depends

from app.models.image_query import ImageQueryResponse, ImageQueryRequest
from app.models.text_query import TextQueryResponse, TextQueryRequest

router = APIRouter(prefix="/search")


@router.get("/text/", response_model=TextQueryResponse)
async def search_by_text(text_query: TextQueryRequest = Depends()) -> TextQueryResponse:
    return NotImplemented


@router.put("/image/", response_model=ImageQueryResponse)
async def search_by_image(image_file: UploadFile, image_query: Annotated[ImageQueryRequest, Depends()]) -> ImageQueryResponse:
    return NotImplemented
