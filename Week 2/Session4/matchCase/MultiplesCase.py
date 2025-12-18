num = int(input("Give me a number.\n"))

match num:
    case a if num % 3 == 0 and num % 5 == 0:
        print("FizzBang")
    case b if num % 3 == 0:
        print("Fizz")
    case c if num % 5 == 0:
        print("Bang")
    case _:
        print("No match")