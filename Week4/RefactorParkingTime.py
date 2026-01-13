timeMinutes = 0
timeHours = 0
maxTime = 120

def convert_minutes(Minutes):
    Hours = Minutes // 60
    Remaining = Minutes % 60
    return Hours, Remaining

def convert_to_minutes(Hours, Remaining):
    Minutes = (Hours*60) + Remaining
    Hours = 0
    return Minutes, Hours

def print_time(Hours, Minutes):
    print(f"Printing ticket for {Hours} Hours and {Minutes} minutes. Total cost is {(Minutes / 30) + (Hours * 2)} pounds")


while True:
    print(f"1. Insert £1 for 30 minutes\n"
          f"2. Insert £2 for 60 minutes\n"
          f"3. Show time remaining\n"
          f"0. Finish and print ticket")
    choice = int(input("Enter your choice: \n"))
    match choice:
        case 1:
            timeMinutes, timeHours = convert_to_minutes(timeHours, timeMinutes)

            if timeMinutes + 30 <= maxTime:
                timeMinutes += 30
                timeHours, timeMinutes = convert_minutes(timeMinutes)
                print(f"Time left has increased to {timeHours} Hours and {timeMinutes} minutes")
            else:
                print("Rejected time left will increase over the maximum allowed time")
                timeHours, timeMinutes = convert_minutes(timeMinutes)

        case 2:
            timeMinutes, timeHours = convert_to_minutes(timeHours, timeMinutes)


            if timeMinutes + 60 <= maxTime:
                timeMinutes += 60
                timeHours, timeMinutes = convert_minutes(timeMinutes)
                print(f"Time left has increased to {timeHours} Hours and {timeMinutes} minutes")
            else:
                print("Rejected time left will increase over the maximum allowed time")
                timeHours, timeMinutes = convert_minutes(timeMinutes)
        case 3:
            print(f"You have {timeHours} Hours and {timeMinutes} minutes left")
        case 0:
            print_time(timeHours, timeMinutes)
            break
        case _:
            print("Invalid choice")