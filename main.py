from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    mixyn: str
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    q += '성공'
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    print(f'{item.name} 요청이 들어왔습니다.')
    print(f'{item.mixyn} 요청이 들어왔습니다.')
    return {"item_name": item.name, "item_id": item_id}

    
@app.get("/tests/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    q += '성공'
    return {"item_id": item_id, "q": q}


def get_full_name(first_name, last_name):
    
    full_name = first_name.title() + " " + last_name.title()
    return full_name
