# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:10:57 2023

@author: 22pw29
"""
"""1. Write a function that returns the sum of all the elements in a specified column 
in a matrix using the following header: 
def sumColumn(m, columnIndex): 
Write a test program that reads a matrix and displays the sum of each 
column. Here is a sample run: """

from typing import List
from random import randint

def getmatrix(row: int, col: int) -> List:
    
    mat: List[List[int]] = []
    
    for i in range(row):
        #rows = input(f"Enter a {row}-by-{col} matrix row for row {i}: ").split(' ')
        rows = [randint(0, 100) for i in range(col)]        
        mat.append([int(i) for i in rows])
    
    return mat

def sumColumn(m: List[List[int]], columnIndex: int) -> int:
    
    colSum: int = 0
    for i in range(len(m)):
        colSum += m[i][columnIndex]
    
    return colSum

def main() -> None:
    
    row: int = int(input("Enter the number of rows in the matrix: "))
    col: int = int(input("Enter the number of columns in the matrix: "))

    mat: List[List[int]] = getmatrix(row, col)
    
    colNum: int = int(input("Enter the column number to get its sum: "))
    colSum: int = sumColumn(mat, colNum)
    
    for i in range(row):
        print(mat[i])

    print(f"\nThe sum of elements for column {colNum} is {colSum}")
    
if __name__ == "__main__":
    main()