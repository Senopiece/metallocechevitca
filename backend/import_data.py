import base64
from io import BytesIO
import asyncio
import aiohttp
import pandas as pd
from tqdm.asyncio import tqdm_asyncio

API_ENDPOINT = "http://localhost:9090/upload/place"
PLACE_ENDPOINT = API_ENDPOINT
IMAGE_ENDPOINT = API_ENDPOINT + "/{xid}/image"


def image_from_base64(image: str) -> BytesIO:
    return BytesIO(base64.b64decode(image, validate=False))


async def post_place(session: aiohttp.ClientSession, row: pd.Series):
    payload = row.to_dict()
    del payload['image']
    payload["embedding"] = eval(payload["embedding"])
    async with session.post(PLACE_ENDPOINT, json=payload) as response:
        if response.status >= 400:
            raise Exception(await response.json())


async def post_image(session: aiohttp.ClientSession, xid: str, image: str):
    async with session.post(IMAGE_ENDPOINT.format(xid=xid),
                            data={"image": image_from_base64(image)}) as response:
        if response.status >= 400:
            raise Exception(await response.json())


async def main():
    async with aiohttp.ClientSession() as session:
        places_tasks = []
        images_tasks = []
        for index, row in preprocessed.sample(2).iterrows():
            places_tasks.append(post_place(session, row))
            for image in eval(row["image"]):
                images_tasks.append(post_image(session, row["XID"], image))

        # Gather all tasks
        await tqdm_asyncio.gather(*places_tasks)
        await tqdm_asyncio.gather(*images_tasks)


if __name__ == '__main__':
    print("Loading data...")
    preprocessed = pd.read_csv("preprocessed.csv").rename(columns={"embeddings": "embedding"})
    print("Loaded!")
    asyncio.run(main())
