from io import BytesIO

import torch
from ray import serve
from starlette.requests import Request
from PIL import Image
from sentence_transformers import SentenceTransformer

from app.adapter import Adapter


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


@serve.deployment
class TextEmbeddingModel:
    def __init__(self):
        self.text_model = SentenceTransformer(
            "sentence-transformers/clip-ViT-B-32-multilingual-v1"
        )
        self.adapter = Adapter().load_state_dict(torch.load("app/adapter.pt", map_location=device))

    async def __call__(self, starlette_request: Request) -> list[float]:
        payload = await starlette_request.json()
        text_emb = self.text_model.encode(payload["text_query"])
        return self.adapter(torch.tensor(text_emb)).detach().numpy().tolist()


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
