n = int(input("How many marks will you enter"))
TotalMarks = 0
Failed = 0
Distinctions = 0

for i in range (1, n + 1):
    Marks = int(input("Enter the marks"))
    TotalMarks += Marks
    if Marks >= 70:
        Distinctions += 1
    elif Marks <= 50:
        Failed += 1

print(f"The total marks you got was {TotalMarks}."
      f"\nYou got {Distinctions} distinctions."
      f"\nYou failed {Failed} subjects."
      f"\nYour average marks was {TotalMarks/n}.")