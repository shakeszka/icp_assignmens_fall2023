phase = input("Is the moon full? If yes enter Full if no enter No: ")
distance = int(input("Enter the distance of the moon from the earth: "))
date = int(input("Enter the date of the month: "))
eclipse = input("Is there an eclipse? Enter True for yes and False for no: ")

modifiers = []

if distance < 230000:
    modifiers.append("Super")

if date in [29,30,31]:
    modifiers.append("Blue")

if eclipse == "True":
    modifiers.append("Blood")

if modifiers:
    print(" ".join(modifiers) + " Moon")
elif phase == "Full":
    # If no modifiers but it's a Full Moon
    print("Full Moon")
else:
    # If none of the conditions are met
    print("Moon")
