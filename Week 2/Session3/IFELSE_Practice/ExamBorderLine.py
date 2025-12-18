score = int(input("Enter your score 0 - 100\n"))
if score >= 38:
    if score > 42 :
        print("Clear Pass")
    else:
        print("Borderline pass, consider review.")
else:
    print("Fail")