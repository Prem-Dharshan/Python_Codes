# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 18:52:47 2023

@author: 22pw29
"""
"""5. Write a function to multiply two matrices. The header of the function is: 
def multiplyMatrix(A, B) 
To multiply matrix A by matrix B, the number of columns in A must be the 
same as the number of rows in B, and the two matrices must have elements of 
the same or compatible types. Let c be the result of the multiplication. Assume 
the column size of matrix A is n. Each element Cij is ai1 * b1j + ai2 * b2j + … 
+ain * bnj. For example, for two matrices A and B, C is 
Write a test program that prompts the user to enter two matrices and displays 
their product."""

from typing import List
from random import randint

def genMat(row: int, col: int):
    
    mat: List[List[int]] = []
    
    for i in range(row):
        mat.append([randint(0,10) for i in range(col)])

    return mat

def multiplyMat(mat1, mat2):
    resMat = [[sum(a * b for a, b in zip(mat1_row, mat2_col))
                            for mat2_col in zip(*mat2)]
                                    for mat1_row in mat1]
    
    return resMat

def main():
    
    mat1, mat2 = genMat(3,3), genMat(3,3)
    print(mat1, "\n\n", mat2)
    print(multiplyMat(mat1, mat2))
    
    return None

if __name__ == "__main__":
    main()