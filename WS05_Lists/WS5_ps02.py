"""When analysing data collected as part of a science experiment it may be desirable to 
remove the most extreme values before performing other calculations. Write a function 
that takes a list of values and an non-negative integer, n, as its parameters. The function 
should create a new copy of the list with the n largest elements and the n smallest 
elements removed. Then it should return the new copy of the list as the function’s only 
result. The order of the elements in the returned list does not have to match the order of 
the elements in the original list. 
Write a main program that demonstrates your function. Your function should read a list 
of numbers from the user and remove the two largest and two smallest values from it. 
Display the list with the outliers removed, followed by the original list. Your program 
should generate an appropriate error message if the user enters less than 4 values. """

from typing import List

def inliersList(lstInp: List[int], n: int ) -> [List, None]:

    lst = lstInp.copy()

    if (len(lst) <= 2 * n):
        raise IndexError (f"Value of {n} is too high")
        return None
    
    for i in range(n):
        lst.remove(max(lst))
        lst.remove(min(lst))
   
    return lst     

def main() -> None:
    
    lst=[]
    l = int(input("Enter the length of the list :"))
    print("Enter the values of the list : ")
    for i in range(l):
        lst.append(int(input("\tEnter an element: ")))
    print("The entered list is: ", lst)

    n = int(input("Enter the number of elements to remove: "))
    
    if (sList := inliersList((lst), n)):
        print("Modified list is :", sList)
        
    return None
    
if __name__ == "__main__":
   main()