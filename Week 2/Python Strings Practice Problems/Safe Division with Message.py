num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
try:
    total = num1 / num2
except ZeroDivisionError:
    print("Cant divide by zero.")
else:
    print(total)
