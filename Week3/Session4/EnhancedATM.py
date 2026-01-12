balance = 0
withdrawnToday = 0
maxWithdrawn = 2000




while True:
    print(f"1. Deposit\n"
          f"2. Withdraw\n"
          f"3. Show balance\n"
          f"4. Show amount withdrawn today\n"
          f"0. Exit")
    choice = int(input("Enter your choice: \n"))
    match choice:
        case 1:
            amount = int(input("Enter the amount of money you want to deposit\n"))
            balance += amount
            print(f"You deposited {amount}\n"
                  f"Your new balance is {balance}")
            input()
        case 2:
            amount = int(input("Enter the amount of money you want to withdraw\n"))
            if amount > balance:
                print("Insufficient money")
            elif withdrawnToday + amount > maxWithdrawn:
                print(f"You will exceed the maximum amount of money you can withdraw by {(withdrawnToday + amount) - maxWithdrawn} pounds")
            else:
                balance -= amount
                withdrawnToday += amount
                print(f"You withdrew {amount}\n"
                      f"Your new balance is {balance}")
            input()
        case 3:
            print(f"Your current balance is {balance}")
            input()
        case 4:
            print(f"You have withdrawn {withdrawnToday} today\n"
                  f"The maximum allowed amount is {maxWithdrawn} pounds\n"
                  f"You have {maxWithdrawn - withdrawnToday} pounds left before you reach the daily limit\n")
            input()
        case 0:
            print("Existing")
            break
        case _:
            print("Invalid choice")
            input()
