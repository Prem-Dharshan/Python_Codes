# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:24:45 2023

@author: 22pw29
"""

"""4) Write a program that calculates the total amount of a meal purchased at a restaurant. The
program should ask the user to enter the charge for the food, then calculate the amounts of a
17 percent tip and 6.5 percent sales tax. Display each of these amounts and total."""

charge = int(input("Enter the Charge of Meal purchased: "))
print(f'''\n\tINVOICE\n
        Charge of the food :\t{charge}\n
        Tip                :\t{charge*0.17}\n
        Sales Tax          :\t{charge*0.065}\n
        Total Amount       :\t{charge+charge*0.65+charge*0.065}'''
        )