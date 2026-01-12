timeMinutes = 0
timeHours = 0
maxTime = 120

while True:
    print(f"1. Insert £1 for 30 minutes\n"
          f"2. Insert £2 for 60 minutes\n"
          f"3. Show time remaining\n"
          f"0. Finish and print ticket")
    choice = int(input("Enter your choice: \n"))
    match choice:
        case 1:
            if (timeMinutes + 30) + (timeHours * 60) <= maxTime:
                timeMinutes += 30
                if timeMinutes % 60 == 0:
                    timeHours += 1
                    timeMinutes = 0
                print(f"Time left has increased to {timeHours} Hours and {timeMinutes} minutes")
            else:
                print("Rejected time left will increase over the maximum allowed time")
        case 2:
            if (timeMinutes) + ((timeHours + 1) * 60) <= maxTime:
                timeHours += 1
                print(f"Time left has increased to {timeHours} Hours and {timeMinutes} minutes")
            else:
                print("Rejected time left will increase over the maximum allowed time")
        case 3:
            print(f"You have {timeHours} Hours and {timeMinutes} minutes left")
        case 0:
            print(f"Printing ticket for {timeHours} Hours and {timeMinutes} minutes. Total cost is {(timeMinutes/30) + (timeHours * 2)} pounds")
            break
        case _:
            print("Invalid choice")
