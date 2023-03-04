from Product import Product
from SupermarketDAO import SupermarketDAO
from CheckoutRegister import CheckoutRegister
from datetime import datetime
from AdminFunctions import AdminFunctions
import hashlib


def main():
    # Welcome statement.
    print("~ Welcome, please select a module ~")
    option = input("Admin | Customer: ")
    # While the input is not equal to ADMIN or CUSTOMER - loop.
    while option.upper() != "ADMIN" and option.upper() != "CUSTOMER":
        print("Incorrect input, please try again.")
        option = input("Admin | Customer: ")
    # If input equals ADMIN, run the admin function.
    if option.upper() == "ADMIN":
        admin()
    # If input equals CUSTOMER, run the customer function.
    elif option.upper() == "CUSTOMER":
        customer()


def admin():
    # Import an instance of AdminFunctions. User: admin1 Pass: admin1
    admin = AdminFunctions()

    admin.read_username_password()

    # Import an instance of the SupermarketDAO.
    admin_dao = SupermarketDAO()

    # while true loop
    while True:
        print(admin.menu())

        # Menu Input.
        menu_input = input("Please enter an option from A - G: ")

        # While not statement to validate the menu inout.
        while menu_input.upper() != 'A' and menu_input.upper() != 'B' and menu_input.upper() != 'C' and menu_input.upper() != 'D' and menu_input.upper() != 'E' and menu_input.upper() != 'F' and menu_input.upper() != 'G':
            menu_input = input("Incorrect input. Please enter an option from A - G: ")

        # Option A
        if menu_input.upper() == 'A':
            barcode_input = input("Enter barcode: ")
            product_name_input = input("Enter product name: ")
            unit_price = float(input("Enter the unit price: "))
            new_product = Product(barcode_input, product_name_input, unit_price)
            admin_dao.add_product_to_db(new_product)

        # Option B
        elif menu_input.upper() == 'B':
            list_product = admin_dao.list_all_products()
            if len(list_product) == 0:
                print("There are zero products listed in the database.")
            else:
                for product in list_product:
                    print(product)

        # Option C
        elif menu_input.upper() == 'C':
            barcode_input = input("Enter barcode: ")
            found = admin_dao.find_product(barcode_input)
            if found is None:
                print("Barcode entered is not recognised.")
            else:
                print(found)

        # Option D
        elif menu_input.upper() == 'D':
            list_transaction = admin_dao.list_all_transcations()
            if len(list_transaction) == 0:
                print("There are zero transactions listed in the database..")
            else:
                for transaction in list_transaction:
                    print(transaction)

        # Option E
        elif menu_input.upper() == "E":
            admin_dao.display_barchart_of_products_sold()

        # Option F
        elif menu_input.upper() == 'F':
            admin_dao.display_excel_report_of_transactions()

        # Option G
        elif menu_input.upper() == 'G':
            exit()


def customer():
    # Import an instance of SupermarketDAO.
    dao = SupermarketDAO()
    # Run the list all function to a temporary list.
    dao_product_list = dao.list_all_products()
    # Open an empty list of items for the dao.list_all_function to appended to.
    products_list = []
    for product in dao_product_list:
        products_list.append(product)

    # Begin the multiple customer while loop
    while True:
        print("Welcome new customer!")

        # Import an instance of the CheckoutRegister
        checkout = CheckoutRegister()

        # Initiate while loop for scanning products
        while True:

            barcode = input("Please enter the barcode of your item: ")
            # Found set to false in order to renew the found variable to false at the start of each loop.
            found = False
            # For loop used to test if the barcode input matches the barcode in the products_list.
            for product in products_list:
                # Run the input against the Product class barcode attribute using the get_barcode function to confirm a match.
                if product.get_barcode() == barcode:
                    # If a match is found, found is set to True and the product is added from the products_list to the selected_products list.
                    found = True
                    selected_products = product
                    break
            # If found = True, then print and scan the product.
            if found:
                print("\n{} - ${}\n".format(selected_products.get_product_name(), float(selected_products.get_price())))
                # Scan_item is called to finish the item selection process - hover of checkout.scan_item for more info.
                checkout.scan_item(selected_products)
                # Save each item into Transaction doc
                checkout.save_transaction(datetime.today(), product.get_barcode(), float(product.get_price()))
            else:
                print("ERROR!! – scanned barcode is incorrect")

            add_item = input("Would you like to scan another item? (Y/N): ")
            # While loop used to prevent the user from not selecting a correct option.
            while add_item.upper() != 'Y' and add_item.upper() != 'N':
                print("Incorrect input, please try again")
                add_item = input("Would you like to scan another item? (Y/N): ")
            # If Y is select the outer scan while loop will continue.
            if add_item.upper() == 'Y':
                continue
            # If N is select both the scan and add_item while loops will break and the program will continue to the next step.
            elif add_item.upper() == 'N':
                break

        payment_amount = checkout.get_total_payment()

        # If a customer enters an incorrect barcode than select N to scan another item, the program automatically restarts itself from the beginning.
        # Without this statement the program would proceed to the payment screen with a due amount of $0 which is pointless.
        if payment_amount == 0:
            continue

        # Initiate while loop for accepting payment
        while True:
            try:
                payment_input = float(input("Payment due: ${}. Please enter an amount to pay: ".format(payment_amount)))
                if payment_input < 0:
                    print("ERROR!! – Negative amounts are not accepted.")
                    continue
                # Use the accept_payment method to accept partial or full amounts until the amount is entirely deducted from the payment_amount.
                checkout.accept_payment(payment_input)
                payment_amount -= payment_input
                if payment_amount <= 0:
                    break
            except ValueError:
                print("Incorrect input, please try again.")
                continue

        # Print receipt
        print(checkout.print_receipt())

        # Next customer
        next_customer = input("Continue to next customer? (Y/N): ")
        while next_customer.upper() != 'Y' and next_customer.upper() != 'N':
            print("Incorrect input, please try again")
            next_customer = input("Continue to next customer? (Y/N): ")
        # If Y is select the outer scan while loop will continue.
        if next_customer.upper() == 'Y':
            continue
        # If N is select both the while loops will break and the program will end.
        elif next_customer.upper() == 'N':
            break


main()
