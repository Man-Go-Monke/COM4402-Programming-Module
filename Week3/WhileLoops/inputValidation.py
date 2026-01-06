while True:
    user = int(input("Enter a positive integer\n"))
    if user <= 0:
        print("enter a number greater than 0\n")
    else:
        print(f"You entered : {user}")
        break