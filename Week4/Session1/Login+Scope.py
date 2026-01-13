def checkpassword(password):
    correct_password = "python123"
    if correct_password == password:
        return True
    else:
        return False



def login():
    password = input("Enter the password")
    IsCorrect = checkpassword(password)
    if IsCorrect == True:
        print("Welcome")
    else:
        print("Access denied")


for i in range (2):
    login()