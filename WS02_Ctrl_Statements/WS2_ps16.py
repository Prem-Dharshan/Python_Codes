#code 16
# List of animals in the Chinese zodiac
animals = ["Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare"]

# Get input from user
year = int(input("Enter a year (e.g. 2000): "))

# Determine the animal associated with the year
animal = animals[year/12 + year % 12]

# Print the animal
print("The animal associated with the year", year, "is:", animal)