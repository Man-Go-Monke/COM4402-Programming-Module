is_student = bool(input("Are you a student. \nYes or No\n"))
age = int(input("How old are you?\n"))
if is_student and age < 18:
    print("Discount applied")
else:
    print("No discount")