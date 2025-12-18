exam = int(input("Enter your exam score 0 - 100\n"))
coursework = int(input("Enter your coursework score 0 - 100\n"))
average = (exam + coursework) / 2
if exam < 35 or coursework < 35:
    print("Automatic fail")
elif average >= 40 :
    print("Module passed")
else :
    print("Module failed")