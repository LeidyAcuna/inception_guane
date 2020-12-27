from typing import Optional, List, Set, Dict

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = Field(None, title="description", max_length=300)
    price: float = Field(..., gt=0, description="price")
    tax: Optional[float] = None
    tags: List[str] = []
    tags_unique: Set[str] = set()
    image: Optional[List[Image]] = None
    
class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.post("/offers")
async def create_offer(offer: Offer):
    return offer

@app.post("/images/multiple")
async def create_multiple_images(images: List[Image]):
    return images

@app.post("/index-weights")
async def create_index_weights(weights: Dict[int, float]):
    return weights

@app.post("/items/{item_id}")
async def post_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items/{item_id}")
async def update_item(*,
                      item_id: int,
                      item: Item,
                      user: User,
                      importance: int = Body(..., gt=0),
                      q: Optional[str] = None
                    ):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results