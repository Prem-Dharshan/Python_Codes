# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 09:38:45 2023

@author: 22pw29
"""

"""3. Design a PayRoll class that has data members for an employee’s hourly pay rate, number
of hours worked, and total pay for the week. Write a program with five PayRoll objects.
The program should ask the user for the number of hours each employee has worked and
will then display the amount of gross pay each has earned. Input Validation: Do not accept
values greater than 60 for the number of hours worked"""

from typing import List
from pyinputplus import inputNum
class PayRoll():
    
    __PAYRATE: int = 100
    __manRate: int 
    __totPay: int
    
    def __init__(self, empHrs: int = 0):
        self.__manRate = empHrs
        self.__totPay = PayRoll.__PAYRATE * self.__manRate
        
    def setPAYRATE() -> None:
        pay = int(input("Set the PAY RATE: "))
        PayRoll.__PAYRATE = pay
        return None
    
    def __str__(self) -> str:
        return f"""{self.__manRate:^10}|{self.__totPay:^10}"""

def main() -> None:

    emp: List[PayRoll] = []
    
    for i in range(5):
        a = inputNum(f"Enter the No of worked hours for Emp Id {i+1:0>2}: ", lessThan=60)
        emp.append(PayRoll(a))


    print(f"|{'Emp ID':^10}|{'Man Rate':^10}|{'Total Pay':^10}")
    for i in range(5):
        print(f"|{i+1:^10}|{emp[i]}|")

if __name__ == '__main__':
    main()
        
    
    