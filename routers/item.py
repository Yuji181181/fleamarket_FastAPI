from fastapi import APIRouter, Path, Query, HTTPException
from cruds import item as item_cruds
from schemas import ItemCreate, ItemUpdate, ItemResponse

router = APIRouter(prefix="/items", tags=["Item"])
## prefix:ルーターの共通のURLを設定する   ## tags:ドキュメントに表示される題名を設定する


# すべてのアイテムを取得するAPI
@router.get("", response_model=list[ItemResponse])
async def find_all():
    return item_cruds.find_all()


# 特定のIDのアイテムを取得するAPI
@router.get("/{id}", response_model=ItemResponse)
async def find_by_id(id: int = Path(gt=0)):
    found_item = item_cruds.find_by_id(id)
    if not found_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_cruds.find_by_id(id)


# 名前でアイテムを検索するAPI
@router.get("/", response_model=list[ItemResponse])
async def find_by_name(name: str = Query(min_length=2, max_length=20)):
    return item_cruds.find_by_name(name)


# 商品を追加するAPI
@router.post("", response_model=ItemResponse)
async def create(item_create: ItemCreate):
    return item_cruds.create(item_create)


# 商品を更新するAPI
@router.put("/{id}", response_model=ItemResponse)
async def update(item_update: ItemUpdate, id: int = Path(gt=0)):
    updated_item = item_cruds.update(id, item_update)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_cruds.update(id, item_update)


# 商品を削除するAPI
@router.delete("/{id}", response_model=ItemResponse)
async def delete(id: int = Path(gt=0)):
    deleted_item = item_cruds.delete(id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_cruds.delete(id)
