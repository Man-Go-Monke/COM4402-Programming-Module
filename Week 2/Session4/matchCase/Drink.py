drink = input("What drink would you like?\ncoffee/tea/water/juice\n")
match drink.lower():
    case "coffee":
        price = 2.50
    case "tea":
        price = 1.80
    case "water":
        price = 1.00
    case "juice":
        price = 1.50
    case _:
        price = 0
print(f"You ordered {drink} for £{price}")
