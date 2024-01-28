# 16) Given an airplane’s acceleration a and take-off speed v, you can compute the minimum
# runway length needed for an airplane to take off using the following formula:

# Write a program that prompts the user to enter in meters/second (m/s) and the acceleration
# in meters/second squared and displays the minimum runway length.

v = int(input("Enter the take off in meters/second (m/s): "))
a = int(input("Enter the acceleration in meters/second squared): "))

print(f"The minimum runway length is {v*v/(2*a)} metres.")
