"""Write the following function that partitions the list using the first element, called a pivot: 
def partition(lst): 
After the partition, the elements in the list are rearranged so that all the elements before 
the pivot are less than or equal to the pivot and the element after the pivot are greater 
than the pivot. The function also returns the index where the pivot is located in the new 
list. For example, suppose the list is [5, 2, 9, 3, 6, 8]. After the partition, the list becomes 
[3, 2, 5, 9, 6, 8]. Implement the function in a way that takes len(lst) comparisons. Write a 
test program that prompts the user to enter a list and displays the list after the partition. 
Here is a sample run: """

from random import randint

def partition(lst):

    #pivot = lst[0]
    
    for i in range(len(lst)-1):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                
    return lst
              
def main():  
    n = int(input("Enter the size of the list: "))
    
    lst = []
    
    for i in range(n):
        lst.append(randint(1, 100))
        
    print(f"Enter a list: {lst}")
    print(f"After the Partition, the list is {partition(lst)}")
    
if __name__ == "__main__":
    main()