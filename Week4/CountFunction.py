count = 0
def add_one(count):
    count = count + 1
    print("Inside:", count)
    return count
count = add_one(count)
print("Outside:", count)