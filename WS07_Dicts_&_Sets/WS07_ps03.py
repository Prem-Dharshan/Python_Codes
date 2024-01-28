# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:48:47 2023

@author: 22pw29
"""
"""3. In the game of Scrabble, each letter has points associated with it. The total
score of a word is the sum of the scores of its letters. More common letters
are worth fewer points while less common letters are worth more points.

Write a program that computes and displays the Scrabble score for a word.
Create a dictionary that maps from letters to point values. Then use the
dictionary to compute the score.The points associated with each letter are
shown below:"""

def scrabbleScore(word: str) -> [int, None]:
    
    if (all(letter.isalpha() for letter in word) == False):
        raise ValueError("Invalid Input")
        return None
    
    scorecard = {
                    "aeilnorstu" : 1,
                    "dg" : 2,
                    "bcmp" : 3,
                    "fhvwy" : 4,
                    "k" : 5,
                    "jx" : 8,
                    "qz" : 10
                }
    
    score: int = 0
    
    for ch in word:
        for key, value in scorecard.items():
            if (ch.lower() in key):
                score += value
    
    return score

def main() -> None:
    
    word = input("Enter a word to calculate the scrabble score: ")
    print(f"The Scrabble Score for the word '{word}' is {scrabbleScore(word)}")
    
    return None    

if __name__ == "__main__":
    main()
                