# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:00:21 2023

@author: 22pw29
"""

"""5. On some basic cell phones, text messages can be sent using the numeric
keypad. Because each key has multiple letters associated with it, multiple
key presses are needed for most letters. Pressing the number once generates
the first letter on the key. Pressing the number 2, 3, 4 or 5 times generates
the second, third, fourth or fifth character listed for that key."""

from typing import Dict

def nokia3300(msg: str) -> str:
    
    keypad: Dict[str, int] = {
        
                ".,?!:" : '1',
                "ABC" : '2',
                "DEF" : '3',
                "GHI" : '4',
                "JKL" : '5',
                "Μ" : '6',
                "N" : "66",
                "O" : "666",
                "PQRS" : '7',
                "TUV" : '8',
                "WXYZ" : '9',
                " " : '0',
    
            }

    dial: str = ""
    
    for i in msg:
        for key, value in keypad.items():
            if (i.upper() in key):
                dial += (value) * (key.rfind(i.upper()) + 1)
                
    return dial

def main() -> None:
    
    msg = input("Enter a message: ")
    print(f"'{msg}' is typed as {nokia3300(msg)} in a dialpad.")
    
    return None

if __name__ == "__main__":
    main()
         