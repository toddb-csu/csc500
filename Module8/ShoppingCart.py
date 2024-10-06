# Todd Bartoszkiewicz
# CSC500
# Module 8: Portfolio Project
# Step 4: Build the ShoppingCart class with the following data attributes and related methods.
# Note: Some can be method stubs (empty methods) initially, to be completed in later steps
class ShoppingCart:
    # Parameterized constructor, which takes the customer name and date as parameters
    # Attributes
    # customer_name (string) - Initialized in default constructor to "none"
    # current_date (string) - Initialized in default constructor to "January 1, 2020"
    # cart_items (list)
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # add_item()
    # Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)

    # remove_item()
    # Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    # If item name cannot be found, output this message: Item not found in cart. Nothing removed.
    def remove_item(self, item_name):
        item_found = False
        for itemToPurchase in self.cart_items:
            if itemToPurchase.item_name == item_name:
                self.cart_items.remove(itemToPurchase)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    # modify_item()
    # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    # If item can be found (by name) in cart,
    # check if parameter has default values for description, price, and quantity.
    # If not, modify item in cart.
    # If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
    def modify_item(self, item_to_purchase_modified):
        item_found = False
        for itemToPurchase in self.cart_items:
            if itemToPurchase.item_name == item_to_purchase_modified.item_name:
                if (itemToPurchase.item_description != "") or (itemToPurchase.item_price != 0.0) or \
                        (itemToPurchase.item_quantity != 0):
                    if (itemToPurchase.item_description != item_to_purchase_modified.item_description) and \
                            (item_to_purchase_modified.item_description != ''):
                        itemToPurchase.item_description = item_to_purchase_modified.item_description
                    if (itemToPurchase.item_price != item_to_purchase_modified.item_price) and \
                            (item_to_purchase_modified.item_price != 0.0):
                        itemToPurchase.item_price = item_to_purchase_modified.item_price
                    if (itemToPurchase.item_quantity != item_to_purchase_modified.item_quantity) and \
                            (item_to_purchase_modified != 0):
                        itemToPurchase.item_quantity = item_to_purchase_modified.item_quantity
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    # get_num_items_in_cart()
    # Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        total_quantity = 0
        for itemToPurchase in self.cart_items:
            total_quantity += itemToPurchase.item_quantity
        return total_quantity

    # get_cost_of_cart()
    # Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        total_cost = 0.0
        for itemToPurchase in self.cart_items:
            total_cost += (itemToPurchase.item_quantity * itemToPurchase.item_price)
        return total_cost

    # print_total()
    # Outputs total of objects in cart.
    # If cart is empty, output this message: SHOPPING CART IS EMPTY
    #
    # Example of print_total() output:
    # John Doe's Shopping Cart - February 1, 2020
    # Number of Items: 8
    # Nike Romaleos 2 @ $189 = $378
    # Chocolate Chips 5 @ $3 = $15
    # Powerbeats 2 Headphones 1 @ $128 = $128
    # Total: $521
    def print_total(self):
        if len(self.cart_items) < 1:
            print("SHOPPING CART IS EMPTY")
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items: {}".format(self.get_num_items_in_cart()))
            for itemToPurchase in self.cart_items:
                itemToPurchase.print_item_cost()
            print("Total: ${:.2f}".format(self.get_cost_of_cart()))

    # print_descriptions()
    # Outputs each item's description.
    #
    # Example of print_descriptions() output:
    # John Doe's Shopping Cart - February 1, 2020
    # Item Descriptions
    # Nike Romaleos: Volt color, Weightlifting shoes
    # Chocolate Chips: Semi-sweet
    # Powerbeats 2 Headphones: Bluetooth headphones
    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Item Descriptions")
        for itemToPurchase in self.cart_items:
            print("{}: {}".format(itemToPurchase.item_name, itemToPurchase.item_description))


class ItemToPurchase:
    # constructor function
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description=""):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

    def print_item_cost(self):
        print("{} {} @ ${:.2f} = ${:.2f}".format(self.item_name, self.item_quantity, self.item_price,
                                                 self.item_quantity * self.item_price))


# Step 5: In the main section of your code, implement the print_menu() function. print_menu() has a ShoppingCart
# parameter and outputs a menu of options to manipulate the shopping cart. Each option is represented by a single
# character. Build and output the menu within the function.
#
# If an invalid character is entered, continue to prompt for a valid choice. Hint: Implement Quit before implementing
# other options. Call print_menu() in the main() function. Continue to execute the menu until the user enters q to Quit.
#
# Example:
# MENU
# a - Add item to cart
# r - Remove item from cart
# c - Change item quantity
# i - Output items' descriptions
# o - Output shopping cart
# q - Quit
# Choose an option:
def print_menu(shopping_cart):
    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print('i - Output items\' descriptions')
    print('o - Output shopping cart')
    print('q - Quit')
    user_input = input('Choose an option: ').lower()

    while user_input != 'q':
        if user_input == 'a':
            # Step 8:
            # Implement Add item to cart menu option.
            #
            # Example:
            # ADD ITEM TO CART
            # Enter the item name:
            # Nike Romaleos
            # Enter the item description:
            # Volt color, Weightlifting shoes
            # Enter the item price:
            # 189
            # Enter the item quantity:
            # 2
            print('ADD ITEM TO CART')
            item_name = input('Enter the item name:\n')
            item_description = input('Enter the item description:\n')
            item_price = input('Enter the item price:\n')
            item_quantity = input('Enter the item quantity:\n')
            if (item_name != '') and (item_price != '') and (item_quantity != ''):
                item_to_purchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            else:
                item_to_purchase = ItemToPurchase()
            shopping_cart.add_item(item_to_purchase)
        elif user_input == 'r':
            # Step 9:
            # Implement remove item menu option.
            #
            # Example:
            # REMOVE ITEM FROM CART
            # Enter name of item to remove:
            # Chocolate Chips
            print('REMOVE ITEM FROM CART')
            item_name = input('Enter the item to remove: ')
            shopping_cart.remove_item(item_name)
        elif user_input == 'c':
            # Step 10:
            # Implement Change item quantity menu option. Hint: Make new ItemToPurchase object before using ModifyItem() method.
            #
            # Example:
            # CHANGE ITEM QUANTITY
            # Enter the item name:
            # Nike Romaleos
            # Enter the new quantity:
            # 3
            print('CHANGE ITEM QUANTITY')
            item_name_modified = input('Enter the item name:\n')
            item_price_modified = 0 #input('Enter the new item price:\n')
            item_quantity_modified = input('Enter the new item quantity:\n')
            item_description_modified = '' #input('Enter the new item description:\n')
            if (item_name_modified != '') and (item_quantity_modified != ''):
                item_to_purchase_modified = ItemToPurchase(item_name_modified, item_price_modified, item_quantity_modified, item_description_modified)
                shopping_cart.modify_item(item_to_purchase_modified)
        elif user_input == 'i':
            shopping_cart.print_descriptions()
        elif user_input == 'o':
            shopping_cart.print_total()
        user_input = input('Choose an option: ').lower()

if __name__ == '__main__':
    # Step 7:
    # In the main section of your code, prompt the user for a customer's name and today's date.
    # Output the name and date. Create an object of type ShoppingCart.
    #
    # Enter customer's name:
    # John Doe
    # Enter today's date:
    # February 1, 2020
    # Customer name: John Doe
    # Today's date: February 1, 2020
    customer_name = input('Enter customer\'s name:\n')
    date_today = input('Enter today\'s name:\n')
    print('Customer name: {}'.format(customer_name))
    print('Today\'s date: {}'.format(date_today))
    shopping_cart = ShoppingCart(customer_name, date_today)
    print_menu(shopping_cart)

# Step 6: Implement Output shopping cart menu option. Implement Output item's description menu option.
#
# Example of shopping cart menu option:
# OUTPUT SHOPPING CART
# John Doe's Shopping Cart - February 1, 2020
# Number of Items: 8
# Nike Romaleos 2 @ $189 = $378
# Chocolate Chips 5 @ $3 = $15
# Powerbeats 2 Headphones 1 @ $128 = $128
# Total: $521
#
# Example of item description menu option.
# OUTPUT ITEMS' DESCRIPTIONS
# John Doe's Shopping Cart - February 1, 2020
# Item Descriptions
# Nike Romaleos: Volt color, Weightlifting shoes
# Chocolate Chips: Semi-sweet
# Powerbeats 2 Headphones: Bluetooth headphones
