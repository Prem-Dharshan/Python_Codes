# code 12
human_years = int(input("Enter the age in human years: "))
if human_years < 0:
  print("Invalid input!")
elif human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = 21 + (human_years - 2) * 4

print(f"The age in dog years is: {dog_years}")
