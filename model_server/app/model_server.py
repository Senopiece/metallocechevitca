from io import BytesIO

from ray import serve
from starlette.requests import Request
from PIL import Image


@serve.deployment
class EmbeddingModel:
    # TODO: decide, how we gonna split text/img embedding, maybe 2 different models
    def __init__(self):
        self.text_model = ...
        self.image_model = ...

    async def __call__(self, starlette_request: Request) -> list[float]:
        # image_payload_bytes = await starlette_request.body()
        # pil_image = Image.open(BytesIO(image_payload_bytes))
        # TODO
        return [1] * 512


embedding_model = EmbeddingModel.bind()

