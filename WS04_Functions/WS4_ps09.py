# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:50:12 2023

@author: 22pw29
"""

"""9.	If you have 3 straws, possibly of differing lengths, it may or may not be possible to lay them down so that they form a triangle when their ends are touching. For example, if all of the straws have a length of 6 inches. then one can easily construct an equilateral triangle using them. However, if one straw is 6 inches. long, while the other two are each only 2 inches. long, then a triangle cannot be formed. In general, if any one length is greater than or equal to the sum of the other two then the lengths cannot be used to form a triangle. Otherwise they can form a triangle. Write a function that determines whether or not three lengths can form a triangle. The function will take 3 parameters and return a Boolean result. In addition, write a program that reads 3 lengths from the user and demonstrates the behaviour of this function."""

from typing import List

def validTriangle(sides: List[int]) -> bool:

    if (sides[0] > sides[1]+sides[2]): return False
    elif (sides[1] > sides[2]+sides[0]): return False
    elif (sides[2] > sides[0]+sides[1]): return False
    else: return True

def main():
    
    side1: int = int(input("Enter side 1: "))
    side2: int = int(input("Enter side 2: "))
    side3: int = int(input("Enter side 3: "))
    
    if validTriangle([side1, side2, side3]):
        print("The 3 sides form a triangle")
    else:
        print("The 3 sides do not form a triangle")

if __name__ == "__main__":
    main()