# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 12:01:26 2023

@author: 22pw29
"""
"""11.	Words like first, second and third are referred to as ordinal numbers. In this exercise, you will write a function that takes an integer as its only parameter and returns a string containing the appropriate English ordinal number as its only result. Your function must handle the integers between 1 and 12 (inclusive). It should return an empty string if a value outside of this range is provided as a parameter. Include a main program that demonstrates your """

def ordinalNumber(num: int) -> str:
    if num == 1:
        return "First"
    elif num == 2:
        return "Second"
    elif num == 3:
        return "Third"
    elif num == 4:
        return "Fourth"
    elif num == 5:
        return "Fifth"
    elif num == 6:
        return "Sixth"
    elif num == 7:
        return "Seventh"
    elif num == 8:
        return "Eighth"
    elif num == 9:
        return "Nineth"
    elif num == 10:
        return "Tenth"
    elif num == 11:
        return "Eleventh"
    elif num == 12:
        return "Twelth"
    else:
        return ""

def main() -> None:
    
    import os
    os.system("pip install prettytable")
    from prettytable import PrettyTable
    
    table = PrettyTable()
    table.field_names = ["Month Number", "Ordinal Number"]

    for i in range(1,13):
        table.add_row([i, ordinalNumber(i)])
    print(table)

    return None
    
if __name__ == '__main__':
    main()