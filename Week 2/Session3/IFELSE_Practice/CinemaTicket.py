Age = int(input("What is your age\n"))
if Age >= 65:
    print("Senior ticket")
elif Age >= 18:
    print("Adult ticket")
elif Age >= 5:
    print("Child ticket")
else:
    print("Free ticket")