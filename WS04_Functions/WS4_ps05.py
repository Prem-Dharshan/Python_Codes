# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:33:09 2023

@author: 22pw29
"""

"""5.	A prime number is an integer greater than 1 that is only divisible by one and itself. Write a function that determines whether or not its parameter is prime, returning True if it is, and False otherwise. Write a main program that reads an integer from the user and displays a message indicating whether or not it is prime"""

def isPrime(num:int) -> bool:
    
    if (num <= 1):
        return False
    
    for i in range(2, int(num**0.5)+1):
        if (num%i == 0):
            return False
    
    return True
    
def main():
    
    if (isPrime(int(input("Enter a number: ")))):
        print("The entered number is a Prime Number")
    else:
        print("The entered number is not a Prime Number")

if __name__ == "__main__":
    main()