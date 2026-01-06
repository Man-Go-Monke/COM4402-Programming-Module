def addNums():
    num1 = int(input("Enter a number\n"))
    num2 = int(input("Enter a second number\n"))
    print(f"The total is {num1 + num2}")

def subtractNums():
    num1 = int(input("Enter a number\n"))
    num2 = int(input("Enter a second number\n"))
    print(f"The total is {num1 - num2}")

while True:
    print(f"\n1. Add"
          f"\n2.Subtract"
          f"\n0.Exit")
    user = int(input())
    match user:
        case 1:
            addNums()
        case 2:
            subtractNums()
        case 0:
            print("Exiting\n")
            break
        case _:
            print("Wrong input\n")

