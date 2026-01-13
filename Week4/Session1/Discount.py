
def apply_discount(price):
    if price > 100:
        discount = 10
    else:
        discount = 0
    final_price = price - discount
    return final_price
p = float(input("Enter price: "))
result = apply_discount(p)
print("Final price:", result)
