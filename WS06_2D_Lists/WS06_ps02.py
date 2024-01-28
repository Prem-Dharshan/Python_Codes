# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:52:13 2023

@author: 22pw29
"""

"""
Suppose the weekly hours for all employees are stored in a table. Each row 
records an employee’s seven-day work hours with seven columns. For 
example, the following table stores the work hours for eight employees. Write 
a program that displays employees and their total hours in decreasing order of 
the total hours. 
"""
from typing import List
from random import randint

def getdata(nEmp: int) -> List:
    
    data: List[List[int]] = []
    
    for i in range(nEmp):
        rows = [randint(0, 9) for i in range(7)]        
        data.append([int(i) for i in rows])
    
    return data

def main() -> None:
    
    data = getdata(7)
    
    rows = len(data)
    print("           Su  M  T  W  Th F  Sa")
    for i in range(rows):
        print(f"Employee {i}", end=' ')
        for j in range(7):
          print(f"{data[i][j]:{' '}>{2}}", end=' ')
        print()

if __name__ == "__main__":
    main()