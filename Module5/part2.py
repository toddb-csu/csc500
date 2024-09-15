# Todd Bartoszkiewicz
# CSC500
# Module 5: Critical Thinking Assignment
# Part 2
# The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased
# each month. The points are awarded as follows:
#
# If a customer purchases 0 books, they earn 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.
# Write a program that asks the user to enter the number of books that they have purchased this month and then display
# the number of points awarded..

if __name__ == '__main__':
    num_books_purchased = int(input('Please enter the number of books purchased this month: '))
    points_earned = 0
    if num_books_purchased >= 8:
        points_earned = 60
    elif num_books_purchased >= 6:
        points_earned = 30
    elif num_books_purchased >= 4:
        points_earned = 15
    elif num_books_purchased >= 2:
        points_earned = 5
    else:
        points_earned = 0

    print('You have been awarded {} points this month'.format(points_earned))
