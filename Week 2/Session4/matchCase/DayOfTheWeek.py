day = int(input("Give me the day number"))
match day:
    case 1:
        print("Monday - Start of work week")
    case 6 | 7:
        print("Weekend - Relax!")
    case _:
        print("Weekday")
