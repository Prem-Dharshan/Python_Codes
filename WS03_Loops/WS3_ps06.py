# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:34:55 2023

@author: 22pw29
"""

from prettytable import PrettyTable

table = PrettyTable(["Temperature in CELSIUS", "Temperature in FAHRENHEIT"])

for i in range(0,21,1):
    table.add_row([f'{i}', f'{1.8 * i + 32:.2f}' ])
    
print(table)