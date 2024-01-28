"""8. Write a hangman game that randomly generates a word and prompts the user to guess 
one letter at a time, as shown in the sample run. Each letter in the word is displayed as an 
asterisk. When the user makes a correct guess, the actual letter is then displayed. When 
the user finishes a word, display the number of misses and ask the user whether to 
continue playing. Create a list to store the words, as follows: 
# Use any words you wish 
words = ["write", "that", "program", ...]"""

import string
import random

len = 7
flag = True
randStr = str(''.join(random.choices(string.ascii_lowercase, k = len)))
inp = []
neg = 0
print(randStr)

while flag:
    
    starCount = 0
    print("(Guess) Enter a letter in word ", end = "")
    for i in randStr:
        if i in inp:
            starCount += 1
            print(i, end = "")
        else:
            print("*", end = "")
            
    j = input(" = ")
    if j not in randStr:
        neg+=1
        print(j, " is not in the word.")
        continue
    
    if j in inp:
        print(j," is already in the word.")
        inp.append(j)
        continue
    
    inp.append(j)
    
    if (len(randStr) == len(inp)):
        flag = False
        
print("The word is ", randStr,". You missed it ", neg," times.")