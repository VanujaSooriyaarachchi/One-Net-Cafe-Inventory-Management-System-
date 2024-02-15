import random

# insert the data in a table format
from tabulate import tabulate

print("\n*****Welcome to One Net Cafe Inventory Management System*****\n")
# dictionary to store item details
items = []


# function to display the console menu
def menu():
    print("Type AID for adding item details.")
    print("Type DID for deleting item details.")
    print("Type UID for updating item details.")
    print("Type VID for viewing the items table.")
    print("Type SID for saving the item details to the text file at any time.")
    print("Type SDD for selecting four dealers randomly from a file.")
    print("Type VRL for displaying all the details of the randomly selected dealers.")
    print("Type LDI for display the items of the given dealer.")
    print("Type ESC to exit the program.")


menu()

inventory = []
random_dealers = []
Duplicate_code = []

while True:
    choice = input("Enter your choice 'AID, DID, UID, VID, SID, SDD, VRL, LDI, ESC : ")

    if choice.upper() == "AID":
        # define a list to store items in the inventory


        def add_item():
            print("Enter the item details.")
            # Handle the exception as desired
            while True:
                try:
                    item_code = int(input("Item Code: "))
                    if item_code < 0:
                        print("Please Enter A Positive Number!")
                    elif item_code in Duplicate_code:
                        print("Duplicate found. Enter a another Item Code.")
                    else:
                        Duplicate_code.append(item_code)
                    break
                except ValueError:
                    print("Please Enter A Valid Code!")
            while True:
                try:
                    item_name = input("Item Name: ")
                    if item_name == "":
                        raise ValueError("Item Name Cannot Be Empty!")
                    break
                except ValueError as ve:
                    print(ve)
            while True:
                try:
                    item_brand = input("Item Brand: ")
                    if item_brand == "":
                        raise ValueError("Item Brand Cannot Be Empty!")
                    break
                except ValueError as ve:
                    print(ve)
            while True:
                try:
                    item_price = float(input("Item Price: "))
                    if item_price < 0:
                        print("Price Cannot Be Negative!")
                    break
                except ValueError:
                    print("Please Enter A Valid Price!")
            while True:
                try:
                    item_quantity = int(input("Item Quantity: "))
                    if item_quantity < 0:
                        print("Quantity Cannot Be Negative!")
                    break
                except ValueError:
                    print("Please Enter A Valid Quantity!")
            while True:
                try:
                    item_category = input("Item Category: ")
                    if item_category == "":
                        raise ValueError("Item Category Cannot Be Empty!")
                    break
                except ValueError as ve:
                    print(ve)
            while True:
                try:
                    purchased_date = str(input("Purchased Date (YYYY-MM-DD): "))
                    break
                except ValueError:
                    print("Please Enter A Valid Date!")
            item = {
                "item_code": item_code,
                "item_name": item_name,
                "item_brand": item_brand,
                "item_price": item_price,
                "item_quantity": item_quantity,
                "item_category": item_category,
                "purchased_date": purchased_date
            }
            inventory.append(item)
            print(inventory)
            print("Item Added Successfully!")


        add_item()

    elif choice.upper() == "DID":

        # function to delete item details from the system
        def delete_item():
            while True:
                try:
                    item_code = int(input("Enter Item Code: "))
                    if item_code < 0:
                        print("Please Enter A Positive Number!")
                        delete_item()
                    break
                except ValueError:
                    print("Please Enter A Valid Code!")
            for item in inventory:
                if item["item_code"] == item_code:
                    inventory.remove(item)
                    print("Item Deleted!")
                    break
            else:
                print("This Item Code NOT Found In The System!")


        delete_item()

    elif choice.upper() == "UID":

        # function to update item details in the system
        def update_item():
            print("Updating an item...")
            item_code = int(input("Enter item code: "))
            for item in inventory:
                if item["item_code"] == item_code:
                    print("Update Details: ")
                    while True:
                        try:
                            item_name = input("Item Name: ")
                            if item_name == "":
                                raise ValueError("Item Name Cannot Be Empty!")
                            break
                        except ValueError as ve:
                            print(ve)
                    while True:
                        try:
                            item_brand = input("Enter item brand: ")
                            if item_brand == "":
                                raise ValueError("Item Brand Cannot Be Empty!")
                            break
                        except ValueError as ve:
                            print(ve)
                    while True:
                        try:
                            item_price = float(input("Enter price: "))
                            if item_price < 0:
                                print("Price Cannot Be Negative!")
                            break
                        except ValueError:
                            print("Please Enter A Valid Price!")
                    while True:
                        try:
                            quantity = int(input("Enter quantity: "))
                            if quantity < 0:
                                print("Quantity Cannot Be Negative!")
                            break
                        except ValueError:
                            print("Please Enter A Valid Quantity!")
                    while True:
                        try:
                            category = input("Enter category: ")
                            if category == "":
                                raise ValueError("Category Cannot Be Empty!")
                            break
                        except ValueError as ve:
                            print(ve)
                    while True:
                        try:
                            purchased_date = str(input("Enter date (YYYY-MM-DD): "))
                            break
                        except ValueError:
                            print("Please Enter A Valid Date!")
                    item["item_name"] = item_name
                    item["item_brand"] = item_brand
                    item["item_price"] = item_price
                    item["item_quantity"] = quantity
                    item["item_category"] = category
                    item["purchased_date"] = purchased_date
                    print(inventory)
                    print("Item Updated!")
                    break

            else:
                print("Item NOT Found!")

        update_item()

    elif choice.upper() == "VID":
        print(inventory)

        # function to view item details in the system
        def view_item():
            # bubble sort the inventory by item_id
            n = len(inventory)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if inventory[j]['item_code'] < inventory[j + 1]['item_code']:
                        inventory[j], inventory[j + 1] = inventory[j + 1], inventory[j]
            # function to view item details in the system
            print(tabulate(inventory, headers="keys", tablefmt="simple_grid", numalign="right"))
        view_item()

    elif choice.upper() == "SID":
        # function to save item details in the text file
        def save_item():
            with open("save_item_data.txt", "w") as f:
                for i in inventory:
                    f.write(str(i))
                    print("Item Saved!")
        save_item()

    elif choice.upper() == "SDD":
        # function to select dealers randomly from text file
        def select_dealers():
            global random_dealers
        with open("dealers.txt", "r") as f:
            # select only 4 dealers
              lines = f.readlines()
              while len(random_dealers) < 4:
                  dealer = random.choice(lines)
                  dealer_name = dealer.split(",")[0]

                # check if the dealer name is already in the list
                  if dealer_name not in [d[0] for d in random_dealers]:
                    random_dealers.append((dealer_name, dealer))
                    print(dealer_name)
              print("4 dealers are selected randomly")

        select_dealers()

    elif choice.upper() == "VRL":
        # function to view dealer's details
        def dealers_details(dealers):
            # Declare a global variable to access outside the function
            global random_dealers
            # Sort the dealers list based on the second element of each tuple using a lambda function
            sorted_dealers = sorted(dealers, key=lambda x: x[1])
            return sorted_dealers

        # Check if the global variable 'random_dealers' is empty
        if not random_dealers:
            print("Please Select the dealer's first.")

        sorted_dealers = dealers_details(random_dealers)

        for dealer in sorted_dealers:
            print(f"Dealer: {dealer[0]}")
            print(f"Details: {dealer[1]}")
            print("_" * 20)

    elif choice.upper() == "LDI":
        # function to show items from randomly selected dealers
        def display_items():
            with open("items.txt", "r") as f:
                lines = f.readlines()

            dealers_items = {}

            # Iterate through each line of input
            for line in lines:
                # Split each line into its four parts
                item, dealers, price, quantity = line.strip().split(", ")
                if dealers.lower() not in dealers_items:
                    dealers_items[dealers.lower()] = []
                dealers_items[dealers.lower()].append((item, price, quantity))

            dealers = []

            for i in range(4):
                dealer_name = input("Enter dealer name {} of 4: ".format(i + 1))
                while dealer_name.lower() not in dealers_items:
                    print("Dealer not found. Please try again.")
                    dealer_name = input("Enter dealer name {} of 4: ".format(i + 1))
                dealers.append(dealer_name.lower())

            print("\n-----------------------------------------------------\n")

            for dealer_name in dealers:
                # Display the dealer's name with the first letter capitalized
                print("Dealer Name: {}".format(dealer_name.capitalize()))
                for item in dealers_items[dealer_name]:
                    print("Item: {}, Price: {}, Quantity: {}".format(item[0], item[1], item[2]))
                print()
        display_items()

    elif choice.upper() == "ESC":
        # function to terminate program
        print("\n*** Thank You! ***\n")
        break

    else:
        # to display the menu options and prompt the user to enter a valid input.
        print("\n*Invalid Input.Try again*\n")
        menu()