NoStudents = int(input("How many students"))
TotalMarks = 0
Distinctions = 0

for i in range (1, NoStudents + 1):
    Marks = int(input("Enter the marks"))
    TotalMarks += Marks
    if Marks >= 70:
        Distinctions += 1
print(f"The total marks is {TotalMarks}."
      f"\n{Distinctions} students got over 70 marks."
      f"\nThe class average is {TotalMarks/NoStudents}")