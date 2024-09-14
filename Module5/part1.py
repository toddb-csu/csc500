# Todd Bartoszkiewicz
# CSC500
# Module 5: Critical Thinking Assignment
# Part 1
# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the total inches of rainfall,
# and the average rainfall per month for the entire period.

if __name__ == '__main__':
    num_years = int(input('Please enter the number of years:'))
    months = {
        0: "January",
        1: "February",
        2: "March",
        3: "April",
        4: "May",
        5: "June",
        6: "July",
        7: "August",
        8: "September",
        9: "October",
        10: "November",
        11: "December"
    }
    rainfall_months = []
    for i in range(num_years):
        for j in range(12):
            rainfall_months.append(int(input('What is the rainfall for the month of {} in inches:'.format(months[j]))))

    # and the average rainfall per month for the entire period
    print('\n{} months had {} total inches of rainfall.'.format(len(rainfall_months), sum(rainfall_months)), end=' ')
    print('The average rainfall per month for the entire period is {:.2f} inches'.format(sum(rainfall_months) / len(rainfall_months)))
