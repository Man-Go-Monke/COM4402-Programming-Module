is_hungry = input("Are you hungry. \nYes or No\n")
if is_hungry.title() == "Yes":
    time_of_day = input("What time of day is it? \nMorning/Afternoon/Evening \n")
    if time_of_day == "Morning":
        print("Have Breakfast")
    elif time_of_day == "Afternoon":
        print("Have Lunch")
    elif time_of_day == "Evening":
        print("have Dinner")
    else:
        print("Have a snack")
else:
    print("Don't eat then")