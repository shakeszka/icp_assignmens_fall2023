def average():
    print("All numbers have to be in range between 0 and 100!")
    firstGrade = int(input("1st grade: "))
    secondGrade = int(input("2nd grade: "))
    thirdGrade = int(input("3rd grade: "))

    average = (firstGrade + secondGrade + thirdGrade) / 3
    print("Average grade:", round(average))
average()
