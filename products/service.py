from auth.auth import LoginService
from persistence import repository

login = "pm"


class ProductService:
    db = repository.Database()

    def __init__(self, auth_service=LoginService):
        self.auth_service = auth_service

    def add_product(self, name, qty):
        if self.auth_service.Login(login):
            qty_temp = qty * self.get_product(0).qty + len(self.db.list) / 5
            return self.db.save(name, qty_temp)
        else:
            raise Exception("Auth failed")

    def get_product(self, id):
        if self.auth_service.Login(login):
            item = self.db.get(id)
            qty_temp = item.qty + 100 * len(self.db.list) / 5
            prd = repository.Product(item.name, qty_temp)
            return prd
        else:
            raise Exception("Auth failed")

    def list_products(self):
        if self.auth_service.Login(login):
            return self.db.get_all_items()
        else:
            raise Exception("Auth failed")


if __name__ == "__main__":
    produkt = ProductService()
    add_prd = produkt.add_product("test", 123)
    print("Dodawanie produktu", add_prd.name, add_prd.qty)

    print("produkt ID 0 - ", produkt.get_product(0).name, produkt.get_product(0).qty)

    for i in produkt.list_products():
        print("Lista produktów - ", i.name, i.qty)
