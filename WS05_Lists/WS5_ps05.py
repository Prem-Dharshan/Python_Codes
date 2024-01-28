"""

Created on Mon Feb  6 10:00:12 2023

@author: 22PW29

"""
""" A line of best fit is a straight line that best approximates a collection of n data points. In 
this exercise, assume that each point in the collection has an x coordinate and a y 
coordinate. The symbols and are used to represent the average x value in the 
collection and the average y value in the collection respectively. The line of best fit is 
represented by the equation y = mx + b where m and b are calculated using the following 
formulas. 
Write a program that reads a collection of points from the user. The user will enter the x 
part of the first coordinate on its own line, followed by the y part of the first coordinate 
on its own line. Allow the user to continue entering coordinates, with the x and y parts 
each entered on their own line, until your program reads a blank line for the x coordinate. 
Display the formula for the line of best fit in the form y = mx +b by replacing m and b with 
the values you calculated using the preceding formulas. 
For example, if the user inputs the coordinates (1, 1), (2, 2.1) and (3, 2.9) then your 
program should display y = 0.95x + 0.1."""

from typing import List

xList: List[float] = []
yList: List[float] = []
n: int = 0

while (a := input("Enter a coordinate (x, y): ") ) != '':
    
    xList.append(float(a.split(',')[0]))
    yList.append(float(a.split(',')[1]))
    n += 1

print(xList , yList)

avgX: float = sum(xList) / len(xList)
avgY: float = sum(yList) / len(yList)
print(avgX,avgY)

pdt: List[float] = []
for i in range(len(xList)):
    pdt.append(xList[i]*yList[i])

squareX = [i*i for i in xList]
m: float = ( sum(pdt) - (sum(xList)*sum(yList)/n) ) / ( sum(squareX) - (sum(xList)**2)/n )
b: float = avgY - m*avgX
print("The equation is: ")
print(f"\ty = {m:.2f}x + {b:.1f}")