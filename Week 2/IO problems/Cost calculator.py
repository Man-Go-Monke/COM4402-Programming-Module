product =  input("Enter product name\n")
price = float(input("Enter the price\n"))
quantity = int(input("Enter quantity\n"))
print("You bought " + str(quantity) + "of " + product +
"\nYour total cost is " + str(price * quantity))