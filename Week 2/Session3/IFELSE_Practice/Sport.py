weather = input("What is the weather like?\nSunny/Rainy/Cold")
mood = input("Mood?\nActive/Tired")
if weather.lower() == "sunny":
    if mood.lower() == "active":
        print("Go for a run")
    elif mood.lower() == "tired":
        print("Relax at the park")
    else:
        print("No suggestion available")
elif weather.lower() == "rainy":
    print("Indoor workout")
elif weather.lower() == "cold":
    print("Go to the gym")
else:
    print("No suggestion available")
