# Todd Bartoszkiewicz
# CSC500
# Module 1: Critical Thinking Assignment
# Part 2
# Write a Python program to find the multiplication and division of two numbers.
# Ask the user to input two numbers (num1 and num2).
# Given those two numbers, multiply them together to find the output.
# Also, divide num1/num2 to find the output.
def multiply(num1, num2):
    print(num1, "*", num2, "is", num1*num2)

def divide(num1, num2):
    print(num1, "/", num2, "is", num1/num2)

if __name__ == '__main__':
    num1 = int(input('Input your first number: '))
    num2 = int(input('Input your second number: '))
    multiply(num1, num2)
    divide(num1, num2)
