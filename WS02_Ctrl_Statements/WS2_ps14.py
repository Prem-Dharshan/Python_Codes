# code 14
# Dictionary of banknotes and their corresponding individuals
banknotes = {1: "George Washington", 2: "Thomas Jefferson", 5: "Abraham Lincoln",
             10: "Alexander Hamilton", 20: "Andrew Jackson", 50: "Ulysses S. Grant", 100: "Benjamin Franklin"}

# Get input from user
denomination = int(input("Enter the denomination of the banknote (e.g. 5): "))

# Check if the denomination is valid
if denomination in banknotes:
    individual = banknotes[denomination]
    print("The individual on the banknote of $",
          denomination, " is:", individual)
else:
    print("Error: Invalid denomination. There is no such note exists.")
