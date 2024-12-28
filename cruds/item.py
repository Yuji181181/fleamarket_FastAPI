from typing import Optional
from enum import Enum


class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"


class Item:
    def __init__(
        self,
        id: int,
        name: str,
        price: int,
        description: Optional[str],
        status: ItemStatus,
    ):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.status = status


items = [
    Item(1, "PC", 100000, "美品です", ItemStatus.ON_SALE),
    Item(2, "スマートフォン", 50000, None, ItemStatus.ON_SALE),
    Item(3, "Python本", 1000, "使用感あり", ItemStatus.SOLD_OUT),
]


# 全てのアイテムを取得する関数
def find_all():
    return items


# 特定のIDのアイテムを取得する関数
def find_by_id(id: int):
    for item in items:  # itemは変数名
        if item.id == id:
            return item
    return None
