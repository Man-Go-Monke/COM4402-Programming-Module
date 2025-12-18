shape = input("Give me a shape type.\ncircle/square/triangle/rectangle\n")
match shape.lower():
    case "circle":
        r = float(input("Give me the radius\n"))
        print(r*3.14**2)
    case "square":
        length = float(input("Give me the length of the square\n"))
        print(length**2)
    case "triangle":
        h = float(input("Give me the height of the triangle\n"))
        b = float(input("Give me the base length of the triangle\n"))
        print((h*b)/2)
    case "rectangle":
        l = float(input("Give me the length of the recangle\n"))
        h = float(input("Give me the length of the recangle\n"))
        print(l*h)
    case _:
        print("Invalid shape")

