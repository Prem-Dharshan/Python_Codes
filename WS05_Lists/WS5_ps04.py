"""An integer, n, is said to be perfect when the sum of all of the proper divisors of n is equal 
to n. For example, 28 is a perfect number because its proper divisors are 1, 2, 4, 7 and 14, 
and 1 + 2 + 4 + 7 + 14 = 28. 
Write a function that determines whether or not a positive integer is perfect. Your 
function will take one parameter. If that parameter is a perfect number then your function 
will return true. Otherwise it will return false. In addition, write a main program 
that uses your function to identify and display all of the perfect numbers between 1 and 
10,000. """

def divisors(n :int ) -> list:
    lst = []
    for i in range(1,n):
        if n % i == 0:
            lst.append(i)
            
    return lst

def isperfect(lst, n : int) -> bool:
    if sum(lst) == n:
        return True
    else:
        return False
    
def main() -> None:
    
    num = int(input("Enter a number to check it's perfection: "))
    
    if (isperfect(divisors(num), num)):
        print(f"{num} is a Perfect number.")
    else:
        print(f"{num} is not a Perfect number.")
        
    lst = []
    print("Printing all the perfect numbers between 1 and 10,000...")
    for i in range(10000):
        if (isperfect(divisors(i), i)):
            lst.append(i)
    
    print(lst)
            
    return

if __name__ == "__main__":
    main()