highest = 0
n = int(input("How many marks will u enter \n"))

for i in range(n):
    mark = int(input("Enter your marks \n"))
    if mark > highest:
        highest = mark

print(f"Your highest mark is {highest}")