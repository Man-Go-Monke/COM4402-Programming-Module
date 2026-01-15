
student_marks = {}#use a dictionary because no duplicates and can do CRUD by key

def add_mark(marks, name, mark):
    marks[name] = mark # create or overwrite
    return marks

def get_mark(marks, name):
    if name in marks:
        return marks[name]
    return None

def update_mark(marks, name, new_mark):
 if name in marks:
    marks[name] = new_mark
    return True
 return False

def delete_mark(marks, name):
    if name in marks:
        del marks[name]
        return True
    return False

