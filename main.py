# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    k = 0
    for i in range(5):
        for j in range(10, 12):
            k += 1
    print(k)
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    num_sales = 7
    if num_sales == 0:
        employee_bonus = 0
    elif num_sales == 1:
        employee_bonus = 2
    elif num_sales == 2:
        employee_bonus = 5
    else:
        employee_bonus = 10
    print(employee_bonus)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
