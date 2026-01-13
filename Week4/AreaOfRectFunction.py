def area_of_rectangle():
    w = float(input("Enter the width: "))
    h = float(input("Enter height: ")) # w and h are local

    return w*h

area = area_of_rectangle()
print(f"The area of this rectangle is: {area}")