# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:43:56 2023

@author: 22pw29
"""

"""8.	Write a function that takes three numbers as parameters, and returns the median value of those parameters as its result. Include a main program that reads three values from the user and displays their median."""

def median(a: int, b: int, c: int) ->int:
    lst =[a,b,c]
    lst.remove(max([a,b,c]))
    lst.remove(min([a,b,c]))
    return lst[0]

def main() -> None:
    
    a:int = int(input("Enter first number: "))
    b:int = int(input("Enter second number: "))
    c:int = int(input("Enter third number: "))
    print(f"Median is {median(a,b,c)}")
    
if __name__ == "__main__":
    main()