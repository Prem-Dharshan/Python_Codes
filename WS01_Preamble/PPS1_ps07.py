"""A vineyard owner is planting several new rows of grapevine, and needs to know how many grapevines to plant in each row. She has determined that after measuring the length of a future row, she can use the following formula to calculate the number of vines that will fit in the row, along with the trellis end-post assemblies that will need to be constructed at each end of the row.
V=R-2ES
Where,
V is the number of grapevines that will fit in the row.
R is the length of the row, in feet.
E is the amount of space, in feet, used by an end-post assembly.
S is the space between the vines, in feet.
Write the program that makes the calculation for the vineyard owner. The program should ask the user to input the following:
The length of the row, in feet
The amount of space used by an end-post assembly, in feet
The amount of space between the vines, in feet
Once the input received, the program should calculate and display the number of grapevines that will fit in the row.
"""

R = int(input("Enter the length of the row, in feet: "))
E = int(input("Enter the amount of space, in feet, used by an end-post assembly: "))
S = int(input("Enter the space between the vines, in feet: "))

print(f"The number of grapevines that will fit in the row is {(R-2*E)/S}")