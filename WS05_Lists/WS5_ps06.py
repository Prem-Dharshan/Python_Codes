""" Write the following function that merges two sorted lists into a new sorted list: 
def merge(list1, list2): 
Write a test program that prompts the user to enter two sorted lists and displays the 
merged list. Here is a sample run:"""

from random import randint

def merge(lst1, lst2):
    return sorted(lst1+lst2)

def main():
    size1 = int(input("Enter the size of list 1: "))
    size2 = int(input("Enter the size of list 2: "))
    
    lst1, lst2= [], []
    
    for i in range(size1):
        lst1.append(randint(0, 100))
   
    for i in range(size2):
        lst2.append(randint(0, 100))
    
    sorted(lst1)
    sorted(lst2)
    
    lst = merge(lst1, lst2)
    
    print(f"\nThe generated lists are..\nL1 -> {lst1}\nL2 -> {lst2}")
    print(f"The merged sorted list is {lst}.")
    
    return

if __name__ == "__main__":
    main()
          

              