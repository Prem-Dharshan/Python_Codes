# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:28:57 2023

@author: 22pw29
"""

"""1. Chris owns an auto repair business and has several employees. If any employee works over
40 hours in a week, he pays them 1.5 times their regular hourly pay rate for all hours over 40.
Design a simple payroll program that calculates an employee’s gross pay, including any
overtime wages.
You design the following algorithm:
Get the number of hours worked.
Get the hourly pay rate.
If the employee worked more than 40 hours:
Calculate and display the gross pay with overtime.
Else:
Calculate and display the gross pay as usual."""

time = int(input("Enter the no. of hours worked: "))
pay = int(input("Enter the wage per hour: "))

print(f"Gross pay is {1.5*pay*(time-40)+pay*40}" if (time>40) else
                        f"Gross pay is {time*pay}")