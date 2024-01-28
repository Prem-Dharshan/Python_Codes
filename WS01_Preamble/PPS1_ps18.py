# 18) Write a program that reads a positive integer, , from the user and then displays the sum of all
# of the integers from to . The sum of the first positive integers can be computed using this
# formula:

num = int(input("Enter a positive number to find the sum of first n numbers: "))
print(f"The sum of the integers from 0 to {num} is {num*(num+1)//2}.")