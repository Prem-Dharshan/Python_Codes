# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 08:59:04 2023

@author: 22pw29
"""

"""15.	Write a recursive function that implements the recurrence relation to calculate the   nth power of an integer value x. Both n and x should be parameters to the function. The return value of the function will be value of xn. For example: if n=4 and x=2 the function should return 24=16. """

def expo(x: int, n: int) -> int:

    if (n != 0):
        return x * expo(x, n-1)
    else :
        return 1
    
def main():
    
    x = int(input("Enter the x: "))
    n = int(input("Enter the n: "))
    
    print("\nThe value of x^n is", expo(x, n), ".\n")
    
    return None

if __name__ == "__main__":
    main()