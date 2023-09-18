year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")

if year >= 1950 and (year - 1950) % 4 == 0:
    print("World Cup year")
elif year >= 1960 and (year - 1960) % 4 == 0:
    print("Euro Cup year")
else:
    pass