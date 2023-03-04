import unittest
from Product import Product
from CheckoutRegister import CheckoutRegister
from SupermarketDAO import SupermarketDAO

class TestProduct(unittest.TestCase):
    """Testing each function of the Product class"""

    product = Product("123", "Milk 2 Litres", float(3.50))

    def test_product_get_barcode(self):
        barcode = self.product.get_barcode()
        self.assertEqual('123', barcode)

    def test_get_product_name(self):
        name = self.product.get_product_name()
        self.assertEqual("Milk 2 Litres", name)

    def test_get_price(self):
        price = self.product.get_price()
        self.assertEqual(float(3.50), price)

class TestCheckoutRegister(unittest.TestCase):
    """Testing functions within the CheckoutRegister class"""

    def test_scan_item(self):
        register = CheckoutRegister()
        product = Product("123", "Milk 2 Litres", float(3.50))
        register.purchase_items.append(product)
        self.assertIn(product, register.purchase_items)

    def test_accept_payment(self):
        register = CheckoutRegister()
        total_owed = 50
        register.accept_payment(total_owed)
        self.assertEqual(register.received_amount, total_owed)

    def test_init(self):
        register = CheckoutRegister()
        self.assertEqual(register.total_payment, 0)
        self.assertEqual(register.received_amount, 0)
        self.assertEqual(len(register.purchase_items), 0)


if __name__ == '__main__':
    unittest()
