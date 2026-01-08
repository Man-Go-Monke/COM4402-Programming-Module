size = 8
for i in range(size):
    line = ""
    for j in range(size):
        if (j+i) % 2 == 0:
            line += "#"
        else:
            line += "."
    print(line)