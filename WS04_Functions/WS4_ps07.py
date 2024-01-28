# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:36:45 2023

@author: 22pw29
"""

"""7.	In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled. Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare as its only result. Write a main program that demonstrates the function."""

def taxiFare(distance: int) -> float:
    return 4 + ((distance//140)*0.25) 

def main() -> None:
    
    dist: int = int(input("Enter distance in kilometers : "))
    print(f"Taxi fare for {dist} km is ${taxiFare(dist):.2f}.")
    
if __name__ == "__main__":
    main()