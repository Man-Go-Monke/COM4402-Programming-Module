rows = 4
counter = 0
for i in range(1, rows+1):
    for j in range(i):
        counter += 1
        print(f"{counter}", end=" ")
    print()