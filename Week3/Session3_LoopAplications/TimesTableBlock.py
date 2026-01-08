for i in range(1, 6):
    line = ""
    for j in range(1, 6):
        line += f"  {j} x {i} = {j*i:<2}"
    print(line.rstrip())