"""8.	Write a program with a loop that asks the user to enter a series of positive numbers. The user should enter a negative number to signal the end of the series. After all the positive numbers have been entered, the program should display their sum."""

series = input("Enter the series of numbers separated by space and enter a negative num to end the series\nEnter here: ").split(' ')

i, sum = 0, 0
while (int(series[i]) > 0):
    sum += int(series[i])
    i += 1
    
print(f"The sum of the series until the negative number is {sum}.")