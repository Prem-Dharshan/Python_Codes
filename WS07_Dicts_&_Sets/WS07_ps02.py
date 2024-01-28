# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 08:43:10 2023

@author: 22pw29
"""

"""Write a program that creates a dictionary containing the names of our states 
as keys and their capital as values. The program should quiz the user by 
displaying the names of a state and asking the user to enter that state’s 
capital. The program should keep a count of the number of correct and 
incorrect responses. """

from typing import Dict
from time import sleep

def quiz(data: Dict[str, str]) -> Dict[str, int]:
    
    score: Dict[str, int] = {
                                "Correct" : 0,
                                "Incorrect" : 0
                            }
    
    for state, capital in data.items():
        
        ans: str = input(f"Enter the capital of the state {state}: ")
        
        if (ans.lower() == capital.lower()): score["Correct"] += 1
        else: score["Incorrect"] += 1
        
        
    return score

def main() -> None:
    
    data = {
                "TamilNadu" : "Chennai",
                "Karnataka" : "Bengaluru",
                "Telugana" : "Hyderabad",
                "Kerala" : "Thiruvanandhapuram",
            }
    print("\nYour Quiz starts in")
    
    for i in range(3,0,-1):
        print(i)
        sleep(1)
    
    print('\a')
    
    result: Dict[str, str] = quiz(data)
    
    print(f"\nThe number of Correct answers is {result['Correct']}")
    print(f"The number of Incorrect answers is {result['Incorrect']}")
    print(f"Your Score is {result['Correct']//len(data)}.")
    
    return None

if __name__ == "__main__":
    main()