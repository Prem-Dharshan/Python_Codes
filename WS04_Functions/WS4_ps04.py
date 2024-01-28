# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:14:39 2023

@author: 22pw29
"""

"""4.	A painting company has determined that for every 115 square feet of wall space, one gallon of paint and eight hours of labor will be required. The company charges $20.00 per hour for labor. Write a program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon. The program should display the following data:
a.	• The number of gallons of paint required
b.	• The hours of labor required
c.	• The cost of the paint
d.	• The labor charges
e.	• The total cost of the paint job
"""

from math import ceil

def userData():
    
    area = int(input("Enter the square feet of wall space to be painted: "))
    price = float(input("Enter the price of the paint per gallon: $"))
    
    return (area, price)

def display():
    
    area, price = userData()
    
    print(f"\nThe number of gallons of paint required is {ceil(area/115)}.")
    print(f"The hours of labor required is {(area/115)*8:.1f}.")
    print(f"The cost of the paint is ${ceil(area/115)*price:.2f}.")
    print(f"The labor charges area ${(area/115)*8*20:.2f}.")
    print(f"The total cost of the paint job is ${ceil(area/115)*price+(area/115)*8*20:.2f}")
        
    return

def main():
    display()
    
if __name__ == "__main__":
    main()