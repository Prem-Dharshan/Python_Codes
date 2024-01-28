# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:42:56 2023

@author: 22pw29
"""

"""1.	Write a function that takes the lengths of the two shorter sides of a right triangle as its parameters. Return the hypotenuse of the triangle, computed using Pythagorean theorem, as the function’s result. Include a main program that reads the lengths of the shorter sides of a right triangle from the user, uses your function to compute the length of the hypotenuse, and displays the result."""

from math import sqrt

def calcHypotenuse(s1, s2):
    return sqrt(s1*s1 + s2*s2)

def main():
    s1 = int(input("Enter the length opposite of the triangle (units): "))
    s2 = int(input("Enter the length adjacent side of the triangle (units): "))
    s3 = calcHypotenuse(s1, s2)
    print(f"\nThe length of the hypotenuse is {s3} units.\n")

if __name__ == "__main__":
    main()
    