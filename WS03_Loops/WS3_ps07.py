"""7.	Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, two pennies the second day, and continues to double each day. The program should ask the user for the number of days. Display a table showing what the salary was for each day, and then show the total pay at the end of the period. The output should be displayed in a dollar amount, not the number of pennies."""

import os
os.system("pip install prettytable")

from prettytable import PrettyTable

days = int(input("Enter the number of days to calculate earning: "))

x = PrettyTable()

x.field_names = ["Day", "Earnings"]

total = 1
for i in range(1,days):
    x.add_row = [f"Day {i}", f"${total/100}.{total%100}"]
    total *= 2

x.add_row = ["Total Earning", total]

print(x)