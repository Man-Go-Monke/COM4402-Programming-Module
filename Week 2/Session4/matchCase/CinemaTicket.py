Age = int(input("What is your age\n"))

match Age:
    case a if Age >= 65:
        print("Senior ticket")
    case b if Age >= 18:
        print("Adult ticket")
    case c if Age >= 5:
        print("Child ticket")
    case _:
        print("Free ticket")