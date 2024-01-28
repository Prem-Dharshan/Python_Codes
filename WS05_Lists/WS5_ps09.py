
"""9. A school has 100 lockers and 100 students. All lockers are closed on the first day of school. 
As the students enter, the first student, denoted S1, opens every locker. Then the second 
student, S2, begins with the second locker, denoted L2, and closes every other locker. 
Student S3 begins with the third locker and changes every third locker (closes it if it was 
open, and opens it if it was closed). Student S4 begins with locker L4 and changes every 
fourth locker. Student S5 starts with L5 and changes every fifth locker, and so on, until 
student S100 changes L100. 
After all the students have passed through the building and changed the lockers, which 
lockers are open? Write a program to find your answer. 
(Hint: Use a list of 100 Boolean elements, each of which indicates whether a locker is open 
(True) or closed (False). Initially, all lockers are closed.) """

lst = [False for k in range(100)]

for i in range(1,100):
    j = i
    while j <= 100:
        lst[j-1] = not lst[j-1]
        j += i
     
print("The lockers opened are: ")
for i in range(len(lst)):
    if lst[i]:
        print(i+1, end=", ")