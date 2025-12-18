Colour = input("What colour. \nRed/Amber/Green\n")
Colour = Colour.lower()

match Colour:
    case "red":
        print("Stop")
    case " amber":
        print("Get ready")
    case "green":
        print("Go")
    case _:
        print("Invalid colour")

