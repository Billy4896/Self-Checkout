import hashlib


class AdminFunctions:

    def read_username_password(self):
        # The login credentials used to access the admin module.
        credentials = "admin1_admin1"
        f = 'Login.bin'
        # Write to the .bin file using a try block.
        try:
            with open(f, "wb") as file:
                file.write(hashlib.sha512(credentials.encode('utf-8')).digest())
                file.close()

        # Throw exception if the file does not exist.
        except FileNotFoundError:
            print("File does not exist, please contact support.")

        # Write to the .bin file using a try block.
        try:
            file = open(f, "rb")
            print("Welcome to the admin module.")
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            p_in = "".join([username, '_', password])
            p_in = hashlib.sha512(p_in.encode('utf-8')).digest()  # Create the hash
            # Read the binary file to a list to test the while loop
            lines = file.read()

        # If the file cannot be found print error statement.
        except FileNotFoundError:
            print("File does not exist, please contact support.")

        # While p_in is not equal to the data in lines - loop user inputs until found.
        while p_in != lines:
            print("Login unsuccessful, please try again.")
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            p_in = "".join([username, '_', password])
            p_in = hashlib.sha512(p_in.encode('utf-8')).digest()  # Create the hash

        # Close the file
        file.close()

    def menu(self):
        # Menu message
        menu = "\nAdministrative System Menu" + "\n"
        menu += "A. Add Products to Database" + "\n"
        menu += "B. List all Products in Database" + "\n"
        menu += "C. Find a Product in the Database" + "\n"
        menu += "D. List All Transactions" + "\n"
        menu += "E. Display a Bar chart of Products sold by quantity" + "\n"
        menu += "F. Display an Excel report of all transactions" + "\n"
        menu += "G. Exit" + "\n"
        return menu


