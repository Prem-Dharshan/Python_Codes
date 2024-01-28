# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:04:49 2023

@author: 22pw29
"""

"""11)	 Write a program to convert the length of the rope in centimeter to
a)	inch
b)	foot
c)	yard
d)	mile
e)	kilometer
Note: Print the results with five decimal approximation.
"""

c = int(input("Enter: "))

print(f"{0.393701*c}")
print(f"{0.03280841666667*c}")
print(f"{0.010936138888889999563*c}")
print(f"{.0000062137*c}")
print(f"{c/1000000}")