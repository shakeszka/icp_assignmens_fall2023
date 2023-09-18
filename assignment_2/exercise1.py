phase = "Full"
distance = 228000
date = 1
eclipse = False

modifiers = []

if distance < 225000:
    modifiers.append("Super")

if date == 2:
    modifiers.append("Blue")

if eclipse:
    modifiers.append("Blood")

if modifiers:
    print(" ".join(modifiers) + " Moon")
elif phase == "Full":
    # If no modifiers but it's a Full Moon
    print("Full Moon")
else:
    # If none of the conditions are met
    print("Moon")
