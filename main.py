from fastapi import FastAPI

from post import Post
from text_populator import TextPopulator

app = FastAPI()

text_populator = TextPopulator()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def create_posts():
    return [
        Post(c, text_populator.random_title(), text_populator.random_content() + " " + text_populator.random_content())
        for c in range(1, 101)
    ]


@app.get("/posts")
async def posts():
    return create_posts()
