# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:35:32 2023

@author: 22pw29
"""
"""
3. Write a function to add two matrices. The header of the function is: def 
addMatrix( A, B )
To add matrix a by matrix b, the number of rows and columns in A must be 
the same as the number of rows and columns in B respectively, and the two 
matrices must have elements of the same or compatible types. Display the 
resultant matix as C."""

from typing import List
from random import randint

def addMatrix(mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    
    # if (len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0])):
    #     return False
    
    rMat: List[List[int]] = []
    
    for i in range(len(mat1)):
        lst = []
        for j in range(len(mat1[i])):
            lst.append(mat1[i][j] + mat2[i][j])
        rMat.append(lst)
            
    return rMat

def main() -> None:
    
    m = int(input("Enter the no. of rows: "))
    n = int(input("Enter the no. of columns: "))
    
    mat1: List[List[int]] = []
    mat2: List[List[int]] = []
    
    for i in range(m):
        l1, l2 = [], []
        for j in range(n):
             l1.append(randint(0, 20))
             l2.append(randint(0, 20))
        mat1.append(l1)
        mat2.append(l2)
        
    rmat = addMatrix(mat1, mat2)
    
    for i in range(m):
        if (i==m//2):
            print(f"{mat1[i]}  +  {mat2[i]}  =  {rmat[i]}")
        else:
            print(f"{mat1[i]}     {mat2[i]}     {rmat[i]}")
            
    return None

if __name__ == "__main__":
    main()