days_late = int(input("How many days late?\n"))

match days_late:
    case a if days_late > 10:
        print("Fine = £10 and membership review")
    case b if days_late >= 6:
        print("Fine = £5")
    case c if days_late >= 1:
        print("Fine = £1")
    case _:
        print("No fine")
