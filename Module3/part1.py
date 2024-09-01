# Todd Bartoszkiewicz
# CSC500
# Module 3: Critical Thinking Assignment
# Part 1
# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food and then calculate the
# amounts with an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total price.

if __name__ == '__main__':
    meal_amount = float(input('Please enter the amount of your meal: $'))
    meal_tip = .18 * meal_amount
    meal_tax = .07 * meal_amount
    meal_total = meal_amount + meal_tip + meal_tax
    print("Meal Tip Amount: ${:.2f}".format(meal_tip))
    print("Meal Tax Amount: ${:.2f}".format(meal_tax))
    print("Meal Total Amount: ${:.2f}".format(meal_total))