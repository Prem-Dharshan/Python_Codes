# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 08:45:48 2023

@author: 22pw29
"""

"""5.	Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The program should first ask for the number of years. The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period."""

# from random import randint
from calendar import month_name

nYears = int(input("Enter the number of years to calculate average rainfall: "))
data, cummData = list(), list()
for i in range(1,nYears+1):
    for j in range(1,13):
        data.append(int(input(f'Enter the inches of rainfall in the Year {i} {month_name[j]}: ')))
        cummData.extend(data)
        # data[i][j] = randint(1, 100)

print(f'The total inches of rainfall is {sum(data)} inches.')
print(f'The average rainfall per month is {sum(data)/(nYears*12):.2f} inch.')