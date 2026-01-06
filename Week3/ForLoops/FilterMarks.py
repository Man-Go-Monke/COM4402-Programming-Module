Pass = 0
n = int(input("How many marks will u enter \n"))

for i in range(n):
    mark = int(input("Enter your marks \n"))
    if mark >= 40:
        print(f"{mark} is a pass ")
        Pass += 1

print(f"You passed {Pass} subjects ")