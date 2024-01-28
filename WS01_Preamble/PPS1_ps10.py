# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 15:56:12 2023

@author: 22pw29
"""

ft = int(input("Enter the height in feet: "))
inch = int(input("Enter the height in inch: "))
kg =  int(input("Enter the weight in pounds: "))/2.2

m = (ft*12 + inch)*0.0254
bmi = kg/(m*m)

print(bmi)
