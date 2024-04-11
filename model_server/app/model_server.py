from io import BytesIO

from ray import serve
from starlette.requests import Request
from PIL import Image
from sentence_transformers import SentenceTransformer


@serve.deployment
class TextEmbeddingModel:
    def __init__(self):
        self.text_model = SentenceTransformer(
            "sentence-transformers/clip-ViT-B-32-multilingual-v1"
        )

    async def __call__(self, starlette_request: Request) -> list[float]:
        payload = await starlette_request.json()
        return self.text_model.encode(payload["text_query"]).tolist()


@serve.deployment
class ImageEmbeddingModel:
    def __init__(self):
        self.image_model = SentenceTransformer("clip-ViT-B-32")

    async def __call__(self, starlette_request: Request) -> list[float]:
        image_payload_bytes = await starlette_request.body()
        pil_image = Image.open(BytesIO(image_payload_bytes))
        return self.image_model.encode(pil_image).tolist()


image_model = ImageEmbeddingModel.options(route_prefix="/image-embedding").bind()
text_model = TextEmbeddingModel.options(route_prefix="/text-embedding").bind()
