balance = 100
user = int(input("Enter a withdraw amount or press 0 to exit\n"))
while balance != 0 and user != 0:
    if balance - user < 0:
        print("Insufficient funds")
    else:
        balance -= user
        print(f"Your new balance is \n{balance}")
    user = int(input("Enter a withdraw amount or press 0 to exit\n"))
print("Exiting")