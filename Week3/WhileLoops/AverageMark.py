Mark = 0
count = 0
while True:
    user = int(input("Enter the students mark\n"
                     "Type -1 to exit\n"))
    if user >=0:
        Mark += user
        count += 1
    elif user < -1:
        print("Cant add negative numbers")
    else:
        break
print(f"You entered {count} marks\n"
      f"The average is {Mark/count}")