# code 15
import math

# Get input from user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

if discriminant > 0:
    # Calculate the real roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The quadratic has 2 real roots:", root1, "and", root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("The quadratic has 1 real root:", root)
else:
    print("The quadratic has no real roots.")
