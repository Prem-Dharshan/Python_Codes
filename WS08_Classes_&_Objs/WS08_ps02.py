# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 08:58:50 2023

@author: 22pw29
"""

"""2. Define a class named GroceryItem. Include private fields that hold an item’s stock number,
price, quantity in stock, and total value. Write a public function named dataEntry() that
calls four private functions. Three of the private functions prompt the user for keyboard
input for a value for one of the data fields stock number, price, and quantity in stock. The
function that sets the stock number requires the user to enter a value between 1000 and
9999 inclusive; continue to prompt the user until a valid stock number is entered. The
functions that set the price and quantity in stock require non-negative values; continue to
prompt the user until valid values are entered. Include a fourth private function that
calculates the GroceryItem’s total value field (price times quantity in stock). Write a public
function that displays a GroceryItem’s values. Finally, write a main() function that declares
a GroceryItem object, assigns values to its fields, and uses the display function."""

from os import system
system('pip install PyInputPlus')
from pyinputplus import inputNum
from typing import List

class GroceryItem:
    
    __stockNo: int
    __price: float
    __qty: int
    __totVal: float
    
    def __init__(self, stockno: int = 0, price: float = 0, qty: int = 0) -> None:
        self.__stockNo = stockno
        self.__price = price
        self.__qty = qty
        self.__totVal = self.__price * self.__qty
        return None
    
    def __setStockNo(self) -> None:
        
        stockno: int

        stockno = inputNum('Enter a stock number: ', min = 1000, lessThan = 9999)
        self.__stockNo = stockno
        return self
    
    def __setPrice(self) -> None:
        price = int(input("Enter the price of the stock: "))
        self.__price = price
        return self
    
    def __setQty(self) -> None:
        qty = int(input("Enter the quantity in stock: "))
        self.__qty = qty
        return self
        
    def __setTotVal(self) -> None:
         self.__totVal = self.__qty * self.__price
         return self
     
    def dataEntry(self) -> None:
         self.__setStockNo()
         self.__setPrice()
         self.__setQty()
         self.__setTotVal()    
         return self
     
    def display(self) -> None:
         print(f"{self.__stockNo:15}{self.__price:15}{self.__qty:15}{self.__totVal:15}")
    
    def __str__(self):
        return f"\n{'Stock No':15}:{self.__stockNo:>15}\
              \n{'Price':15}:{self.__price:>15}\
              \n{'Quantity':15}:{self.__qty:>15}\
              \n{'Total Value':15}:{self.__totVal:15}"
        
def main() -> None:
    
    pomato= GroceryItem()

    print(pomato)
    pomato.dataEntry()
    # pomato.display()
    print(pomato)
    
    return None

if __name__ == '__main__':
    main()