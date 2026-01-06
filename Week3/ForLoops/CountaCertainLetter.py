Number = int(input("How many names are you entering\n"))
Count = 0
NamesList = []
for i in range (Number):
    name = input("Enter the name")
    NamesList.append(name)
letter = input("Enter a letter you want to count\n")
for i in NamesList:
    for char in i:
        if char.lower() == letter.lower():
            Count += 1
            break

print(f"There are {Count} amount of stored names that contain the letter {letter}")

