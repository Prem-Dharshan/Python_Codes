# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:42:45 2023

@author: 22pw29
"""

"""1. Design a class that holds the following personal data: name, address, age, and phone
number. Write appropriate accessor and mutator functions. Demonstrate the class by
writing a program that creates three instances of it. One instance should hold your
information, and the other two should hold your friends’ or family members’ information."""


class personalData:
    
    __name: str
    __addr: str
    __age: int
    __phNo: int
    
    def __init__(self, name: str, address: str, age: int, phno: int):
        
        self.name = name
        self.addr = address
        self.age = age
        self.phNo = phno
        
    def __str__(self):
        
        return f"""{'Name':15}:{self.name:>15}\
                   \n{'Address':15}:{self.addr:>15}\
                   \n{'Age':15}:{self.age:>15}\
                   \n{'Phone number':15}:{self.phNo:>15}
                """
        
     
def main() -> None:
    
    me: object = personalData("DPD", "Unknown", 19, "Confidential")
    frnd1: object = personalData("Thithiksha", "Vedanthangal", 3, 92534346572)
    frnd2: object = personalData("Beks", "Keezhpaakam", "47", 9876545678)
    
    print(me, frnd1, frnd2, sep='\n')
    
    return None

if __name__ == "__main__":
    main()