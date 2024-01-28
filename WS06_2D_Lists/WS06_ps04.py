# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:09:14 2023

@author: 22pw29
"""

"""4. In numerical analysis, a sparse matrix is a matrix in which most of the 
elements are zero. Here, substantial memory requirement reductions can be 
realized by storing only the non-zero entries. One such format is Coordinate 
List (CL), which stores sparse matrix as a list (row, column, value) tuples. 
Write a program to accept a sparse matrix and print its CL format. For 
example, consider the following sparse matrix and its Coordinate list format. 
"""
from typing import List

def genSparseMat(mat: List[List[int]]):
    
    smat: List[List[int]] = []
    smat.append(["R", "C", "Elt"])
    
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if (mat[i][j] != 0):
                smat.append([i,j,mat[i][j]])
                
    return smat

def main():
    
    row: int = int(input("Enter the number of rows in the matrix: "))
    col: int = int(input("Enter the number of columns in the matrix: "))
    mat: List[List[int]] = []

    for i in range(row):
        rows = input(f"Enter a {row}-by-{col} matrix row for row {i}: ").split(' ')
        mat.append([int(i) for i in rows])
    
    smat: List[List[int]] = genSparseMat(mat)
    
    print(smat)
    
    return None

if __name__ == "__main__":
    main()
    