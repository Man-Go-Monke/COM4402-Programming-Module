balance = 0
def Deposit(amount, balance):
    if amount > 0:
        balance += amount

    else:
        print("Cant add negative money to account")
    return balance



def Withdraw(amount, balance):
    if balance - amount >= 0:
        balance -= amount
    else:
        print("Insufficient money")
    return balance



while True:
    print(f"1. Deposit\n"
          f"2. Withdraw\n"
          f"3. Show balance\n"
          f"0. Exit")
    choice = int(input("Enter your choice: \n"))
    match choice:
        case 1:
            amount = int(input("Enter the amount of money you want to deposit\n"))
            balance = Deposit(amount, balance)
            print(f"You deposited {amount}\n"
                  f"Your new balance is {balance}")
            input()
        case 2:
            amount = int(input("Enter the amount of money you want to withdraw\n"))
            balance = Withdraw(amount, balance)
            print(f"You withdrew {amount}\n"
                      f"Your new balance is {balance}")
            input()
        case 3:
            print(f"Your current balance is {balance}")
            input()
        case 0:
            print("Existing")
            break
        case _:
            print("Invalid choice")
            input()
