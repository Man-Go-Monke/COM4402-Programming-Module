size = 5
for i in range(1, size + 1):
    line = ""
    for j in range(1, size + 1):
        if i == 1 or i == size:
            line += f"*"
        else:
            if j == 1 or j == size:
                line += f"*"
            else:
                line += f" "
    print(line)