rows = 5

for i in range(1, rows+1):
    for j in range(i):
        print(f"*", end=" ") #end=" " makes it so the stars are printed on the same line and the print() makes it so that it starts a new line after the row is done
    print()