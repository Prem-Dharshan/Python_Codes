# 20) In the United States, fuel efficiency for vehicle is normally expressed in miles-per-gallon
# (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers
# (L/100 km).
# Create a program that reads a value from the user in American units and displays the
# equivalent fuel efficiency in Canadian Units.

mpg = int(input("Enter the fuel efficiency for your vehicle (miles per gallon): "))
print("The equivalent fuel efficiency in Canadian Units is {0:.2f} L/100km.".format(235.2145*mpg))