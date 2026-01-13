rate = 0.2
amount = int(input("How much money"))

def calculate_tax(amount):
    return amount * rate

tax = calculate_tax(amount)
print(tax)
