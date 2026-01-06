secret = 17
guess = 0
while guess != 17:
    guess = int(input("guess a number\n"))
    if guess > 17:
        print("Too high")
    elif guess < 17:
        print("Too low")
print("correct")