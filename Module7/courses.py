# Todd Bartoszkiewicz
# CSC500
# Module 7: Critical Thinking Assignment
#
if __name__ == '__main__':
    # Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the
    # courses meet.
    course_room_numbers = {
        'CSC101': '3004',
        'CSC102': '4501',
        'CSC103': '6755',
        'NET110': '1244',
        'COM241': '1411'
    }

    # The program should also create a dictionary containing course numbers and the names of the instructors that teach
    # each course.
    course_instructors = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee'
    }

    # The program should also create a dictionary containing course numbers and the meeting times of each course.
    course_meeting_times = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.'
    }

    # The program should let the user enter a course number and then it should display the course's room number,
    # instructor, and meeting time.
    course_number = input('Please enter the course number: ')

    # and the average rainfall per month for the entire period
    if course_number in course_room_numbers:
        print('{} is in room {}, {} is the instructor, and the course meets at {}'.
              format(course_number, course_room_numbers[course_number], course_instructors[course_number],
                     course_meeting_times[course_number]))
    else:
        print('Course, {}, couldn\'t be found'.format(course_number))
