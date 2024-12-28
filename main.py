from fastapi import FastAPI
from cruds import item as item_cruds


app = FastAPI()


# すべてのアイテムを取得するAPI
@app.get("/items")
async def find_all():
    return item_cruds.find_all()


# 特定のIDのアイテムを取得するAPI
@app.get("/items/{id}")
async def find_by_id(id: int):
    return item_cruds.find_by_id(id)


# 名前でアイテムを検索するAPI
@app.get("/items/")
async def find_by_name(name: str):
    return item_cruds.find_by_name(name)
