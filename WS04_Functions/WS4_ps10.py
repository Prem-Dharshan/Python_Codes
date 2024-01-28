# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:58:28 2023

@author: 22pw29
"""
"""10.	Write a function named precedence that returns an integer representing the precedence of a mathematical operator. A string containing the operator will be passed to the function as its only parameter. Your function should return 1 for + and -, 2 for * and /, and 3 for ˆ. If the string passed to the function is not one of these operators then the function should return -1. Include a main program that reads an operator from the user and either displays the operator’s precedence or an error message indicating that the input was not an operator. """

def precedence(operator: str) -> int:

    if operator in '+-': return 1
    elif operator in '*/': return 2
    elif operator == '^': return 3
    else: return -1
    
def main() -> None:
    
    a: str = input("Enter the operator: ")

    if (precedence(a) == -1):
        raise TypeError ("Input is not an operator")
    else:
        print(f"Precedence of {a} is {precedence(a)}.")

if __name__=="__main__":
    main()
    