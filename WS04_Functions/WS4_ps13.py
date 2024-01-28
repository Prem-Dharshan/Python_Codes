# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:49:51 2023

@author: 22pw29
"""

"""13.	Write a function that determines how many days there are in a particular month. Your function will take two parameters: The month as an integer between 1 and 12, and the year as a four digit integer. Ensure that your function reports the correct number of days in February for leap years. Include a main program that reads a month and year from the user and displays the number of days in that month."""

from calendar import month_name

def isLeap(year: int) -> bool:
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def daysInAMonth(month: int, year: int) -> int:
    
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        if isLeap(year):
            return 29
        else:
            return 28
        
def main() -> None:
    
    month: int = int(input("Enter the month number (1-12): "))
    year: int = int(input('Enter the year: '))
    print (f"{month_name[month]} month in {year} has {daysInAMonth(month, year)} days")
    
if __name__ == '__main__':
    main()