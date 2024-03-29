"""1. Write a program that reads integers from the user and stores them in a list. Your program 
should continue reading values until the user enters 0. Then it should display all of the 
values entered by the user (except for the 0) in order from smallest to largest, with one 
value appearing on each line. Use either the sort method or the sorted function to sort 
the list 
"""
def main() -> None:
    
    li = list()
    while (x := int(input("Enter a number (Press 0 to end the input): "))):
        li.append(x)
    
    print(f"The original list is {li}.")
    print(f"The sorted list is {sorted(li)}.")
    
    return None

if __name__ == "__main__":
    main()