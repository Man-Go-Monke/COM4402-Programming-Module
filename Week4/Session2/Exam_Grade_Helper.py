def classify_mark(marks: int) -> str:

    if marks > 100 or marks < 0:
        raise ValueError
    if not type (marks) is int:
        raise TypeError
    if marks < 40:
        return "Fail"
    elif marks >= 40 and marks < 70:
        return "Pass"
    else:
        return "Distinction"








def calculate_summary(marks: list[int]):
    total = 0
    fail_count = 0
    distinction_count = 0
    average = 0
    for i in marks:
        outcome = classify_mark(i)
        total += i
        if outcome == "Fail":
            fail_count += 1
        elif outcome == "Distinction":
            distinction_count += 1
    try:
        average = total / len(marks)
    except ZeroDivisionError:
        print("Cant divide by zero")
    return int(total), float(average), int(fail_count), int(distinction_count)





