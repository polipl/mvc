import unittest
from auth.auth import LoginService
from products.service import ProductService


class TestUnit(unittest.TestCase):
    def test_add_product_fails_on_login_failures(self):
        class TestLoginService(LoginService):
            def Login():
                return False

        with self.assertRaises(Exception):
            service = ProductService(auth_service=TestLoginService)
            service.add_product("qwe", 123)


if __name__ == "__main__":
    unittest.main()
