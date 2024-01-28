# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 15:43:27 2023

@author: 22pw29
"""
"""
9) Design and implement an interactive program that reads an amount in rupees as an integer
and determines and prints the minimum number of bills of Rs. 50, Rs. 20, Rs. 10, Rs. 5, and
Rs. 1 denominations in it. For example, if the amount is Rs. 179, your program should print
that it consists of three 50, one 20, zero 10, one 5, and four 1 bills.
"""

amt = int(input("Enter an amount in rupees: "))
deno = [50,20,10,5,1]
print("You will need ", end="")
for i in deno:
    print(f"{amt//i} {i},", end = " ")
    amt%=i
print("notes.")