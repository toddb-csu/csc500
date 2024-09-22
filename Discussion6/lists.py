if __name__ == '__main__':
    # List of temperatures
    weekly_temperatures = [98.1, 101.0, 97.6, 96.1, 94.6, 90.3, 88.1]

    # Print the average temperature
    print("Average temperature this week: ", sum(weekly_temperatures) / len(weekly_temperatures))

    # Remove the first temperature in the list
    weekly_temperatures.remove(98.1)
    # Add a new temperature to the end of the list
    weekly_temperatures.append(89.3)
    # Update the 2nd temperature in the list
    weekly_temperatures[1] = 100.9
    # Add a temperature to the middle of the list
    weekly_temperatures.insert(4, 95.5)

    print(weekly_temperatures)

    # Remove the last temperature and store it in another variable
    last_temperature = weekly_temperatures.pop()
    print("last_temperature:", last_temperature)
    # Add another array of temperatures onto the end of the first array
    weekly_temperatures.extend([90.2, 91.2, 93.2, 94.2, 95.2, 96.2])
    # Add another lists of temperatures to the end of the array in another way
    weekly_temperatures[len(weekly_temperatures):] = [97.2, 98.2]

    print(weekly_temperatures)

    # multi-dimensional array of values
    temps_last_4weeks = [['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                         [98.1, 101.1, 97.1, 96.1, 94.1, 90.1, 88.1],
                         [98.2, 101.2, 97.2, 96.2, 94.2, 90.2, 88.2],
                         [98.3, 101.3, 97.3, 96.3, 94.3, 90.3, 88.3],
                         [98.4, 101.4, 97.4, 96.4, 94.4, 90.4, 88.4]]

    for i in range(len(temps_last_4weeks)):
        print(temps_last_4weeks[i])
