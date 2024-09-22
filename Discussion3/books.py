# Management book title recommendations that I would like to read
management_book_title_recommendations = ['The Making of a Manager', 'The Silo Effect', 'Measure What Matters',
                                         'Dare to Lead', 'Now, Discover Your Strengths', 'Indistractable',
                                         'Talking to Strangers', 'The Harvard Business Review Manager\'s Handbook',
                                         'Helping People Change', 'Creative Calling', 'Permission to Screw Up',
                                         'Brave New World', 'Creating an Effective Management System',
                                         'The First-Time Manager', 'First, Break All the Rules',
                                         'The Ordinay Leader', 'Radical Candor', 'Start Finishing']

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    action = input("Would you like to add or remove a book?")
    if action == "add":
        management_book_title_recommendations.append(input("What title would you like to add?"))
    elif action == "remove":
        management_book_title_recommendations.remove(input("What title would you like to remove?"))

    # Print the list of management books I would like to read
    print("Management books I would like to read: ", management_book_title_recommendations)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
