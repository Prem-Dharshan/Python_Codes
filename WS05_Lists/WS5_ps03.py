"""3. Write a program that reads words from the user until the user enters a blank line. After 
the user enters a blank line your program should display each word entered by the user 
exactly once. The words should be displayed in the same order that they were entered. 
For example, if the user enters: 
first 
second 
first 
third 
second 
then your program should display: 
first 
second 
third """

lst = []

print("Start entering words and press enter without an input to exit.")
while (inp:=input("Enter: ")) != "":
    if inp not in lst:
        lst.append(inp)
    
print("The words entered were", *lst, ".")
    
    