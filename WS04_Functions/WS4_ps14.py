# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 08:43:51 2023

@author: 22pw29
"""

"""13.	Many recipe books still use cups, tablespoons and teaspoons to describe the volumes of ingredients used when cooking or baking. While such recipes are easy enough to follow if you have the appropriate measuring cups and spoons, they can be difficult to double, triple or quadruple when cooking Christmas dinner for the entire extended family. For example, a recipe that calls for 4 tablespoons of an ingredient requires 16 tablespoons when quadrupled. However, 16 tablespoons would be better expressed (and easier to measure) as 1 cup. Write a function that expresses an imperial volume using the largest units possible. The function will take the number of units as its first parameter, and the unit of measure (cup, tablespoon or teaspoon) as its second parameter. Return a string representing the measure using the largest possible units as the function’s only result.For example, if the function is provided with parameters representing 59 teaspoons then it should return the string “1 cup, 3 tablespoons, 2  teaspoons”. Hint: One cup is equivalent to 16 tablespoons. One tablespoon is equivalent to 3 teaspoons."""

def unitConverter(teaspoon):
    
    cup = teaspoon//48
    tablespoon = (teaspoon%48)//3
    teaspoon = (teaspoon%48)%3
    
    return cup, tablespoon, teaspoon

def main():
    
    teaspoons = int(input("Enter the number of teaspoons: "))
    units = unitConverter(teaspoons)

    print(f"{teaspoons} teaspoons is equivalent to {units[0]} Cups, {units[1]} Tablespoons and {units[2]} Teaspoons.\n")

if __name__=="__main__":
    main()