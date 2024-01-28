# code 5
books = int(input("Enter the number of books purchased: "))
points = 0

if books == 1:
    points = 5
elif books == 2:
    points = 15
elif books == 3:
    points = 30
elif books >= 4:
    points = 60

print(f"Points earned: {points}")