# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:41:36 2023

@author: 22pw29
"""

"""2. The date June 10, 1960, is special because when it is written in the following format, the
month times the day equals the year: 6/10/60."""

date = input("Enter the date (dd/mm/yy): ").split('/')
print("It's a magic year" if int(date[0])*int(date[1]) == int(date[2]) 
                          else "Not a magic year")