# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:01:38 2023

@author: 22pw29
"""

"""6.	In a particular jurisdiction, 
taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare as its only result. 
Write a main program that demonstrates the function"""

def fareCalc(distance) -> float:
    
    return 4 + (distance*1000/140) * 0.25

def main() -> None:
    
    distance =  float(input("Enter the distance travelled: "))
    
    print(f"The total fare for the distance travelled is {fareCalc(distance):.2f}.")
    
if __name__ == "__main__" :
    main()