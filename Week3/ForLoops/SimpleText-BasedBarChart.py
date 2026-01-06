Bars = []

numbers = int(input("How many bars u want"))
for i in range(numbers):
    BarSize = int(input("enter a number to determine the size of this bar"))
    Bars.append(BarSize)
for i in Bars:
    Bar = ""
    for x in range(i):
        Bar += "*"
    print(Bar)
