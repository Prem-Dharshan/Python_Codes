""" A bug collector collects bugs every day for seven days. Write a program that keeps a running total of the number of bugs collected during the seven days. The loop should ask for the number of bugs collected for each day, and when the loop is finished, the program should display the total number of bugs collected.
"""

bugs = 0

for i in range(1,8):
    bugs += int(input(f"Enter the number of bugs collected on Day {i} : "))

print(f"\nThe total number of bugs collected is {bugs}.\n\n")