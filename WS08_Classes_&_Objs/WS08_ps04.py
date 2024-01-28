# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 08:52:12 2023

@author: 22pw29
"""

"""4. Define a class called Cricket that will describe the members Player name, Team name, and
Batting average. Write a program to getData details of ‘n’ players using getData(). Define two
member functions with same name Display() using function overloading concept, the first
member function Display(), takes no argument, which prints the details of a player of the
corresponding object, and the second Display() takes object as argument, which prints the
details of player."""

from os import system
system('pip install multipledispatch')
from multipledispatch import dispatch

class Cricket:
    pass

class Cricket:
    
    playerName: str
    teamName: str
    battingAvg: float
    
    def __init__(self, playerName: str, teamName: str, battingAvg: float):
        self.playerName = playerName
        self.teamName = teamName
        self.battingAvg = battingAvg
    
    def getData(self):
        self.playerName = input("Enter player name: ")
        self.teamName = input("Enter team name: ")
        self.battingAvg = float(input("Enter batting average: "))
    
    @dispatch()
    def display(self):
        print("Player Name: {}\nTeam Name: {}\nBatting Average: {}\n".format(self.playerName, self.teamName, self.battingAvg))

    @dispatch(object)
    def display(self, obj: Cricket):
        print(f"Player Name: {obj.playerName}\nTeam Name: {obj.teamName}\nBatting Average: {obj.battingAvg}\n")

def main() -> None:
    n = int(input("Enter the number of players: "))

    players = []
    for i in range(n):
        p = Cricket("", "", 0.0)
        p.getData()
        players.append(p)

    print("Details of each player using the display with one parameter function:\n")
    for p in players:
        p.display()

    print("Details of each player using the Display with two parameter function:\n")
    for p in players:
        p.display(p)
    
    return

if __name__ == '__main__':
    main()
