import uuid

from src.common.database import Database

class Item():
    def __init__(self, sku, desc, _id=None):
        self.desc = desc
        self.sku = sku
        self._id = sku[-4:]

    @classmethod
    def get_by_sku(cls, sku):
        return cls(**Database.find_one('items', {'sku': sku}))

    def json(self):
        return {
            "_id": self._id,
            "sku": self.sku,
            "desc": self.desc
        }

    def save_to_mongo(self):
        Database.insert('items', self.json())