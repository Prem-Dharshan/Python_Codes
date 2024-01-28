# code 13
# Get input from user
month = input("Enter the month (e.g. March): ")
day = int(input("Enter the day (e.g. 20): "))

# Determine season based on input
if month == "December" and day >= 21 or month == "January" or month == "February":
    season = "Winter"
elif month == "March" and day < 20 or month == "April" or month == "May":
    season = "Spring"
elif month == "June" and day < 21 or month == "July" or month == "August":
    season = "Summer"
elif month == "September" and day < 22 or month == "October" or month == "November":
    season = "Fall"

# Print the season
print("The season is:", season)
