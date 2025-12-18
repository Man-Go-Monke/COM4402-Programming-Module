days_late = int(input("How many days late?\n"))
if days_late > 10:
    print("Fine = £10 and membership review")
elif days_late >= 6:
    print("Fine = £5")
elif days_late >= 1:
    print("Fine = £1")
else:
    print("No fine")