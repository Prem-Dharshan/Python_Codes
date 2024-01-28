# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 09:02:32 2023

@author: 22pw29
"""

"""
    Running on a particular treadmill you burn 3.9 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
"""

for i in range(10,31,5):
    print(f"The number of calories after {i} minutes is {3.9*i:.2f} kal")