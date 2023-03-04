from Transcation import Transcation
from SupermarketDAO import SupermarketDAO

class CheckoutRegister:
    """The class required to run the checkout."""

    def __init__(self):
        """Initialise attributes for CheckoutRegister class."""
        self.total_payment = 0.0
        self.received_amount = 0.0
        self.purchase_items = []

    def get_total_payment(self):
        """A simple function to return the total payment."""
        return self.total_payment

    def accept_payment(self, partial_amount):
        """A function to accept a certain amount of payment and increment it to the received amount attribute."""
        self.received_amount += partial_amount
        return self.received_amount

    def scan_item(self, products):
        """A function used to increment the product price to the total payment amount and append it to the purchase_items list."""
        self.total_payment += float(products.get_price())
        self.purchase_items.append(products)

    def print_receipt(self):
        """A function for printing the customer receipt."""
        message = "\n----- Final Receipt-----"
        message += "\n"
        for p in self.purchase_items:
            message += p.get_product_name()+" "+"$"+str(p.get_price())+"\n"

        message += "\n"
        message += "Total amount due: $"+str(self.total_payment)+"\n"
        message += "Amount received: $"+str(self.received_amount)+"\n"
        message += "Balance given: $"+str(self.received_amount-self.total_payment)+"\n"
        return message

    def save_transaction(self, current_date, barcode_information, price_information):
        """A function to save the transaction"""
        current_date = current_date
        barcode_information = barcode_information
        price_information = price_information
        trans = Transcation(current_date, barcode_information, price_information)
        dao = SupermarketDAO()
        dao.add_transactions_to_db(trans)



