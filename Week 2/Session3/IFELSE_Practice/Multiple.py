num = int(input("Give me a number.\n"))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBang")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Bang")
else:
    print("No match")