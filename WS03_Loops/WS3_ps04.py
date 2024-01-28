# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 09:25:54 2023

@author: 22pw29
"""

import os
os.system("pip install prettytable")
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Hour", "Distance travelled"]

speed = int(input("Enter speed in mph: "))
n = int(input("Enter the number of hours travelled: "))

for i in range(1,n+1):
    table.add_row([i, speed*i])

print(table)