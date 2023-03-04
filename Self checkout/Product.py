
class Product:
    """A product class required for the CheckoutRegister class."""

    def __init__(self, barcode, product_name="", unit_price=0.0):
        """Initialise attributes for Product class."""
        self.__barcode = barcode
        self.__product_name = product_name
        self.__unit_price = unit_price

    def get_barcode(self):
        """A simple function to return the barcode number."""
        return self.__barcode

    def get_product_name(self):
        """A simple function to return a product name."""
        return self.__product_name

    def get_price(self):
        """A simple function to return a unit price."""
        return self.__unit_price

    def __str__(self):
        return self.__barcode + " " + self.__product_name + " " + self.__unit_price

