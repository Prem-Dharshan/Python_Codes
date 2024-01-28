# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 09:16:23 2023

@author: 22pw29
"""

amt = float(input("Enter the budget : "))
n = int(input("Enter number of expenses: "))
tot = 0

for i in range(n):
  exp = int(input("Enter expense : "))
  amt -= exp

print(f"You are Rs.{-amt:2f} under budget." if amt < 0 else f"You have Rs.{amt:.2f} left.")
