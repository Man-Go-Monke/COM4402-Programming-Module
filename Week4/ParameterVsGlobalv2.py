def calculate_tax(amount, rate):

    return amount*rate

amount = int(input("Enter ur money"))
rate = 0.2
tax = calculate_tax(amount, rate)
print(tax)