# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:00:56 2023

@author: 22pw29
"""

"""3.	There are three seating categories at a stadium. For a softball game, Class A seats cost $15, Class B seats cost $12, and Class C seats cost $9. Write a program that asks how many tickets for each class of seats were sold, and then displays the amount of income generated from ticket sales."""

def ticketsSold() -> tuple:
    
    classA = int(input("Enter the number of tickets sold in Class A: "))
    classB = int(input("Enter the number of tickets sold in Class B: "))
    classC = int(input("Enter the number of tickets sold in Class C: "))    
    
    return (classA, classB, classC)

def incomeCalculater() -> None:
    
    A, B, C = ticketsSold()
    
    print(f"\nThe amount of income generated from ticket sales is ${A*15 + B*12 + C*9}.")
    
    return

def main() -> None:
    incomeCalculater()
    return

if __name__ == "__main__":
    main()