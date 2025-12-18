PIN = int(input("Enter the PIN"))
if PIN == 1234:
    sec = input("What is your favourite colour")
    if sec.lower() == "blue":
        print("Access granted")
    else:
        print("Incorrect")
else:
    print("Incorrect")