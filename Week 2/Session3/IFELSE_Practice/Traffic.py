Colour = input("What colour. \nRed/Amber/Green\n")
Colour = Colour.lower()
if Colour == "red":
    print("Stop")
elif Colour == "amber":
    print("Get ready")
elif Colour == "green":
    print("Go")
else:
    print("Invalid colour")