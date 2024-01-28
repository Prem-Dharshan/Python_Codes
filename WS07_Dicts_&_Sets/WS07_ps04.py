# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 09:03:55 2023

@author: 22pw29
"""

"""4. In a Canadian postal code, the first, third and fifth characters are letters
while the second, fourth and sixth characters are numbers. The province
can be determined from the first character of a postal code, as shown in the
following table. No valid postal codes currently begin with D, F, I, O, Q,
U, W, or Z.
The second character in a postal code identifies whether the address is rural
or urban. If that character is a 0 then the address is rural. Otherwise it is
urban."""

from typing import Dict

def inputvalidator(pincode: str) -> bool:
    
    if (pincode[0] in "DFIOQUWZ"):
        raise ValueError("Invalid input: Pincode starts with an invalid code.")
        return False
    
    if all(code.isalpha() for code in pincode[::2]) == False:
        raise ValueError("Invalid input: Invalid pincode.")
        return False
    
    if all(code.isdigit() for code in pincode[1::2]) == False:
        raise ValueError("Invalid input: Invalid pincode.")
        return False
        
    return True

def locator(pincode: str) -> None:
    
    provinces: Dict = {
                        "A" : "Newfoundland",
                        "B" : "Nova Scotia",
                        "C" : "Prince Edward Island",
                        "E" : "New Brunswick",
                        "GHJ" : "Quebec",
                        "KLMNP" : "Ontario",
                        "R" : "Manitoba",
                        "S" : "Saskatchewan",
                        "T" : "Alberta",
                        "V" : "British Columbia",
                        "X" : "Nunavut or Northwest Territories",
                        "Y" : "Yukon"
                        # "H" : "Alagan Harees",
                    }

    if (pincode[1] == str(0)):
        print("The postal code is for a rural ", end='')
    else:
        print("The postal code is for an urban ", end='')
        
    for key, value in provinces.items():
        if (pincode[0] in key):
            print(f"address in {value}.")
    
    return None
            
def main() -> None:
    
    postalcode = input("Enter a valid postal code (T2N 1N4): ").replace(' ', '')
    
    if (inputvalidator(postalcode)):
        locator(postalcode)
        
    return None

if __name__ == "__main__":
    main()