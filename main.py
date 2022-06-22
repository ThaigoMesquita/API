from optparse import Option
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"WishList"}


@app.get("/items/{item_id}")
async def read_item(produto: str, descrição: Optional[str]= None,link: Optional[str]= None, foto: Optional[str]= None ):
    return {"produto": produto, "link": link, "foto": foto,  "descrição":descrição  }


