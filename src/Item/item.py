import uuid

from src.common.database import Database

class Item():
    def __init__(self, sku, desc, claimed, stock, _id=None):
        self.desc = desc
        self.sku = sku
        self.claimed = claimed
        self.stock = stock
        self._id = sku[-4:]

    @classmethod
    def get_by_sku(cls, sku):
        return cls(**Database.find_one('items', {'sku': sku}))

    def json(self):
        return {
            "_id": self._id,
            "sku": self.sku,
            "desc": self.desc,
            "claimed": self.claimed,
            "stock": self.stock
        }

    def save_to_mongo(self):
        Database.update('items', {"_id": self._id}, self.json())