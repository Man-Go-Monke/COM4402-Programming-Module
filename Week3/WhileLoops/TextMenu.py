last_name = ""
while True:
    print(f"\n1.Store name"
          f"\n2.View last name entered"
          f"\n0.Exit")
    user = int(input())
    match user:
        case 1:
            user = input("Enter the name")
            last_name = user

        case 2:
            if last_name == "":
                print("No names entered yet")
            else:
                print(last_name)
        case 0:
            print("Exiting\n")
            break
        case _:
            print("Wrong input\n")

