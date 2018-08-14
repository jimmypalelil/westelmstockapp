import uuid

from src.common.database import Database

class Item():
    def __init__(self, sku, desc, _id=None):        
        self.desc = desc
        self._id = sku

    @classmethod
    def get_by_sku(cls, sku):
        return cls(**Database.find_one('items', {'sku': sku}))

    def json(self):
        return {
            "sku": self.sku,
            "desc": self.desc
        }

    def save_to_mongo(self):
        Database.insert('items', self.json())
