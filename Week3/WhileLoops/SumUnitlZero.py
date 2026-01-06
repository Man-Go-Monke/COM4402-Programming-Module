sum = 0

while True:
    user = int(input("Enter a number press 0 to stop\n"))
    sum += user
    if user == 0:
        break
print(f"The sum is {sum}")
