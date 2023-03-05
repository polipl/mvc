from .model import Product
import random


class Database:
    list = []

    def __init__(self):
        for i in range(0, 10):
            self.list.append(
                Product(
                    "Produkt-%s" % str(random.randint(0, 100)), random.randint(0, 100)
                )
            )

    def save(self, name, qty):
        self.list.append(Product(name, qty))
        return Product(name, qty)

    def get(self, id):
        return self.list[id]

    def get_all_items(self):
        return self.list

