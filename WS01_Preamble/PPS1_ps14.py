# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:19:32 2023

@author: 22pw29
"""

"""Write a program to get radius as input from the user and print the following results with three decimal approximation
a)	Diameter
b)	Area
c)	Circumference of the circle 
Hint: Use value of pi as 3.1415927
"""

r = int(input("Enter: "))
print(f"{2*r} {3.1415927*r*r} {2*3.1415927*r}")