Letter = input("Give me the letter grade.\nA/B/C/D/F")
match Letter.upper():
    case "A":
        print("80-100")
    case "B":
        print("70-79")
    case "C":
        print("51-69")
    case "D":
        print("41-50")
    case "F":
        print("0-40")
    case _:
        print("Invalid Grade")