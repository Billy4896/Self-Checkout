class Transcation:
    """A transcation class required for the CheckoutRegister class"""

    def __init__(self, current_date, barcode, amount):
        """Initialise attributes for Product class."""
        self.__current_date = current_date
        self.__barcode = barcode
        self.__amount = amount

    def __str__(self):
        return self.__current_date + " " + self.__barcode + " " + self.__amount

    def get_current_date(self):
        """A simple function to return the current date."""
        return self.__current_date

    def get_barcode(self):
        """A simple function to return a barcode."""
        return self.__barcode

    def get_amount(self):
        """A simple function to return the amount."""
        return self.__amount
