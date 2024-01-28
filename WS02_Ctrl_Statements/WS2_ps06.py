# code 6
pos = input("Enter the position : ")
if ((pos[0] in "aceg") and (pos[1] in "1357")) or ((pos[0] in "bdfh") and (pos[1] in "2468")):
  print("Square is black")
else:
  print("Square is white")
