""". Write a program that identifies all of the words in a string entered by the user. Begin by 
writing a function that takes a string of text as its only parameter.Your function should 
return a list of thewords in the string with the punctuation marks at the edges of the words 
removed. The punctuation marks that you must remove include commas, periods, 
question marks, hyphens, apostrophes, exclamation points, colons, and semicolons. Do 
not remove punctuation marks that appear in the middle of a words, such as the 
apostrophes used to form a contraction. For example, if your function is provided with 
the string "Examples of contractions include: don’t, isn’t, and wouldn’t." then your 
function should return the list ["Examples", "of", "contractions", "include", "don’t", 
"isn’t", "and", "wouldn’t"]. 
Write a main program that demonstrates your function. It should read a string from the 
user and display all of the words in the string with the punctuation marks removed."""

from typing import List

def stripStr(a: str) -> List[str]:
    lst = a.split()
    for i in range(len(lst)):
        if lst[i][-1] in " ,:;.!?-":
            lst[i] = lst[i][:len(lst[i])-1]
    return lst

def main() -> None:
    a:str = input("Enter the sentence :")
    print(stripStr(a))       

if __name__ == "__main__":
    main()