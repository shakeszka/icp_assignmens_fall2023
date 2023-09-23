def average():
    firstGrade = int(input("1st grade: "))
    secondGrade = int(input("2nd grade: "))
    thirdGrade = int(input("3rd grade: "))

    average = (firstGrade + secondGrade + thirdGrade) / 3
    print("Average grade:", round(average))
average()
