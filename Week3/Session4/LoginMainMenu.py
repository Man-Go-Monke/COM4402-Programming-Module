def login_then_menu():
    correct_user = "admin"
    correct_password = "python123"

    attempts = 0
    maxAttempts = 3

    while attempts < maxAttempts:
        username = input("Username: ")
        password = input("Password: ")

        if username == correct_user and password == correct_password:
            print("Login Successful")
            break
        else:
            print("Incorrect Username or Password")
            attempts += 1

    if attempts >= maxAttempts:
        print("Login Failed")
        return
    while True:
        userChoice = int(input(f"1: Greetings\n"
                               f"2: Show Username\n"
                               f"0: Log off\n"))
        match userChoice:
            case 1:
                print("Greetings")
            case 2:
                print(f"Your username is {correct_user}")
            case 0:
                print("Logging off")
                return
            case _:
                print("Invalid Choice")
login_then_menu()
