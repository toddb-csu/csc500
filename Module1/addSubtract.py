# Todd Bartoszkiewicz
# CSC500
# Module 1: Critical Thinking Assignment
# Part 1
# Write a Python program to find the addition and subtraction of two numbers.
# Ask the user to input two numbers (num1 and num2).
# Given those two numbers, add them together to find the output.
# Also, subtract the two numbers to find the output.
def add(num1, num2):
    print(num1, "+", num2, "is", num1+num2)

def subtract(num1, num2):
    print(num1, "-", num2, "is", num1-num2)

if __name__ == '__main__':
    num1 = int(input('Input your first number: '))
    num2 = int(input('Input your second number: '))
    add(num1, num2)
    subtract(num1, num2)
