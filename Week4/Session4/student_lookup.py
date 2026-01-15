students = {
 "Aisha": 85,
 "Bilal": 72,
 "Chen": 90
}

def find_mark(students, name):
    if  not type(name) is str or not type(students) is dict:
        raise TypeError
    else:
        if name in students:
            return students[name]
        else:
            return None


