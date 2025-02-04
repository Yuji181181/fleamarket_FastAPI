from fastapi import APIRouter, Body
from cruds import item as item_cruds

router = APIRouter(prefix="/items", tags=["Item"])
## prefix:ルーターの共通のURLを設定する   ## tags:ドキュメントに表示される題名を設定する


# すべてのアイテムを取得するAPI
@router.get("")
async def find_all():
    return item_cruds.find_all()


# 特定のIDのアイテムを取得するAPI
@router.get("/{id}")
async def find_by_id(id: int):
    return item_cruds.find_by_id(id)


# 名前でアイテムを検索するAPI
@router.get("/")
async def find_by_name(name: str):
    return item_cruds.find_by_name(name)


# 商品を追加するAPI
@router.post("")
async def create(item_create=Body()):
    return item_cruds.create(item_create)


# 商品を更新するAPI
@router.put("/{id}")
async def update(id: int, item_update=Body()):
    return item_cruds.update(id, item_update)


# 商品を削除するAPI
@router.delete("/{id}")
async def delete(id: int):
    return item_cruds.delete(id)
