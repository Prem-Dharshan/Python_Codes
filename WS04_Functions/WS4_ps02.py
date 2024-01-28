# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:56:55 2023

@author: 22pw29
"""

"""2.	Write a function that takes two positive integers that represent the numerator and denominator of a fraction as its only two parameters. The body of the function should reduce the fraction to lowest terms and then return both the numerator and denominator of the reduced fraction as its result. For example, if the parameters passed to the function are 6 and 63 then the function should return 2 and 21. Include a main program that allows the user to enter a numerator and denominator. Then your program should display the reduced fraction."""

from math import gcd

def reducedFraction(nume: int, deno: int) -> (int, int):
    return (nume//gcd(nume, deno), deno//gcd(nume, deno))

def main() -> None:
 
    n = int(input("Enter a numerator :"))
    d = int(input("Enter a denominator :"))
    print(f"The reduced fraction is {reducedFraction(n, d)[0]}/{reducedFraction(n, d)[1]}")

    return None

if __name__=="__main__":
    main()