# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# GKumataka, 8.20.2021, Started script creation.
# GKumataka, 8.21.2021, Updated product class.
# GKumataka, 9.1.2021, Started file processor code.
# Gkumataka, 9.7.2021, Finalized and tested code.
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        GKumataka, 8.20.2021,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    # Product Name
    @property
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Cannot have numbers in the name!")

    # Product Price
    @property
    def product_price(self):  # (getter or accessor)
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, value):  # (setter or mutator)
        try:
            self.__product_price = float(value)
        except Exception as e:
            raise Exception("Price must be numeric!")

    # -- Methods --
    def __str__(self):
        return self.product_name + ', ' + self.product_price



# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    @staticmethod
    def add_data_to_list(name, price, lstOfProductObjects):
        """ Adds new user input data
        :param product: (string) product name to add.
        :param price: (string) product price to add
        :param lstOfProductObjects: (list) of dictionary rows
        :return:(list) of dictionary rows
        """
        product_new = Product(name, price)  # class instance
        lstOfProductObjects.append(product_new)  # save the instance object to list
        print("New data was added to the list")
        return lstOfProductObjects

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Write data to a file from a list of dictionary rows
         :param file_name: (string) with name of file
         :param list_of_product_objects: (list) of product data saved to file
         :return: (bool) with status of success status

         changelog: (When,Who,What)
         GKumataka, 8.21.2021, created main portion of save data code
         """

        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_product_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            raise e
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Read data from file
         :param file_name: (string) with name of file
         :param list_of_product_rows: (list) of product rows in file
         :return: (bool) with status of success status

         changelog: (When,Who,What)
         GKumataka, 9.1.2021, created main portion of read data code
         """

        list_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(',')
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("There was an error")
        return list_of_product_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks

    methods:
    print_menu_choices: prints menu choices to choose from
    input_menu_choice: gets input from user to move forward
    print_current_data_in_list: prints current list data
    input_yes_no_choice: determines if input is yes or no
    add_new_data: gets new data to add to list
    changelog: (When,Who,What)
        GKumataka, 9.1.2021, Created Class
    """

    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_choices():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options:
        1) Show current data
        2) Add new data
        3) Save data to file
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_data_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current data in the file: *******")
        for row in list_of_rows:
            print(row.product_name + ', ' + str(row.product_price))
        print("*******************************************")

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def add_new_data():
        # Asks for inputs and returns values
        while True:
            name = input("Please enter the a name for the product: ")
            if name.strip().isnumeric() == False:
                name = name
                price = float(input("Please enter a price for the product: "))
                if type(price) == float:
                    price = price
                    check = Product(product_name=name, product_price=price)
                else:
                    print("Price input is not numeric!")
                    print("Please start over!")
                    break
            else:
                print("Name is not a string!")
                print("Please start over!")
                break
            return check

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while True:
    #IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_choices()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Show current data
        IO.print_current_data_in_list(lstOfProductObjects)  # Calls IO function and returns variables
        continue  # to show the menu'

    elif strChoice.strip() == '2':
        lstOfProductObjects.append(IO.add_new_data())  # Calls IO function and returns variables
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)  #Saving file
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit