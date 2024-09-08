# Todd Bartoszkiewicz
# CSC500
# Module 4: Portfolio Milestone
# Step 1: Build the ItemToPurchase class with the following specifications:
#
# Attributes
# item_name (string)
# item_price (float)
# item_quantity (int)
# Default constructor
# Initializes item's name = "none", item's price = 0, item's quantity = 0
# Method
# print_item_cost()
# Example of print_item_cost() output:
# Bottled Water 10 @ $1 = $10
class ItemToPurchase:
    # constructor function
    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print("{} {} @ ${:.2f} = ${:.2f}".format(self.item_name, self.item_quantity, self.item_price, self.item_quantity * self.item_price))

# Step 2: In the main section of your code, prompt the user for two items and
# create two objects of the ItemToPurchase class.
# Example:
# Item 1
# Enter the item name:
# Chocolate Chips
# Enter the item price:
# 3
# Enter the item quantity:
# 1
# Item 2
# Enter the item name:
# Bottled Water
# Enter the item price:
# 1
# Enter the item quantity:
# 10
if __name__ == '__main__':
    print("Item 1")
    item_name = input('Enter the item name:\n')
    item_price = float(input('Enter the item price:\n'))
    item_quantity = int(input('Enter the item quantity:\n'))
    item_to_purchase1 = ItemToPurchase(item_name, item_price, item_quantity)

    print("Item 2")
    item_name = input('Enter the item name:\n')
    item_price = float(input('Enter the item price:\n'))
    item_quantity = int(input('Enter the item quantity:\n'))
    item_to_purchase2 = ItemToPurchase(item_name, item_price, item_quantity)

    print("TOTAL COST")
    item_to_purchase1.print_item_cost()
    item_to_purchase2.print_item_cost()
    print("Total: ${:.2f}".format((item_to_purchase1.item_price * item_to_purchase1.item_quantity) +
                                  (item_to_purchase2.item_price * item_to_purchase2.item_quantity)))
