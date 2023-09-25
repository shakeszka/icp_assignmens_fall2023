def get_grade(score):
    if score < 63:
        return "F"
    elif 63 <= score < 67:
        return "D"
    elif 67 <= score < 70:
        return "D+"
    elif 70 <= score < 73:
        return "C-"
    elif 73 <= score < 77:
        return "C"
    elif 77 <= score < 80:
        return "C+"
    elif 80 <= score < 83:
        return "B-"
    elif 83 <= score < 87:
        return "B"
    elif 87 <= score < 90:
        return "B+"
    elif 90 <= score < 95:
        return "A-"
    else:
        return "A"

while True:
    score = int(input("Score: "))

    if 0 <= score <= 100:
        grade = get_grade(score)
        print(f"Your grade is {grade}")
        break
    else:
        print("Invalid input. Please enter a score between 0 and 100.")

    