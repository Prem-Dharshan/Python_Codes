# code 11
sides = int(input("Enter the number of sides of a shape: "))

if sides < 3 or sides > 10:
    print("Invalid input. Number of sides should be between 3 and 10.")
elif sides == 3:
    print("The shape is a triangle.")
elif sides == 4:
    print("The shape is a quadrilateral.")
elif sides == 5:
    print("The shape is a pentagon.")
elif sides == 6:
    print("The shape is a hexagon.")
elif sides == 7:
    print("The shape is a heptagon.")
elif sides == 8:
    print("The shape is an octagon.")
elif sides == 9:
    print("The shape is a nonagon.")
else:
    print("The shape is a decagon.")
