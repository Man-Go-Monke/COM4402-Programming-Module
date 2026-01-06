password = "123python"
while True:
    user = input("Enter the correct password\n")
    if user == password:
        print("access granted")
        break
    else:
        print("wrong password")