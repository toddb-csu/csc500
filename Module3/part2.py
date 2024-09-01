# Todd Bartoszkiewicz
# CSC500
# Module 3: Critical Thinking Assignment
# Part 2
# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Write a Python program to solve the general version of the above problem.
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.

if __name__ == '__main__':
    current_time = int(input('Please enter the current hour of the time: '))
    hours_to_wait = int(input('How many hours to wait for the alarm? '))
    alarm_time = (current_time + hours_to_wait) % 24
    print("The alarm will go off at", alarm_time)