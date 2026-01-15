seats = [] # used a list because we are changing values and they need to be ordered

def create_row(names):
    for name in names:
        seats.append(name)

def get_student_at(row, index):
    return seats[index]

def swap_seats(row, index1, index2):
    seats[index1], seats[index2] = seats[index2], seats[index1]

def remove_student(row, name):
    seats.pop(name)