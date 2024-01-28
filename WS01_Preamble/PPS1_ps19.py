# 19) In many jurisdictions a small deposit is added to drink containers to encourage people to
# recycle them. In one particular jurisdiction, drink containers holding one liter or less have a
# $0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit.
# Write a program that reads the number of containers of each size from the user. Your
# program should continue by computing and displaying the refund that will be received for
# returning those containers. Format the output so that it includes a dollar sign and always
# exactly two decimal places.

deposit = 0

while (True):
    inp = float(input("Enter the number of containers of each size in litres (Press 0 to exit): "))
    
    if (inp >0 and inp <= 1): 
        deposit += 0.10
    elif (inp >1): 
        deposit += 0.25
    else: 
        print("Invalid Input")
        break 

print("The refund received for returning the containers is ${:.2f}.".format(deposit))