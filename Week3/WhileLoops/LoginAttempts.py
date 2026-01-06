username = "Me"
password = "123python"
attempts = 0
while True:
    Pass = input("Enter the correct password\n")
    User = input("Enter the username\n")
    if User == username and Pass == password:
        print("Login successful")
        break
    elif attempts >= 3:
        print("Account Locked")
        break
    else:
        print("Wrong password or username")
        attempts += 1
