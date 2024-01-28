# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 09:49:59 2023

@author: 22pw29
"""
"""
12. write a function that determines whether or not a password is good. We will define a good password to be a one that is at least 8 characters long and contains at least one uppercase letter, at least one lowercase letter, and at least one number. Your function should return true if the password passed to it as its only parameter is good. Otherwise it should return false. Include a main program that reads a password from the user and reports whether or not it is good.
"""
import os
os.system("pip install re")
from re import search


def isValidPassword(password):

    while (len(password) >= 8):

        if (search("[a-z]", password) and
            search("[A-z]", password) and
                search("[0-9]", password)):
            return True
        else:
            return False
    else:
        return False


def main():

    password = input("\nEnter a password to check validity: ")

    if (isValidPassword(password)):
        print("\nThe entered password is a Valid Password")
    else:
        print("\nThe entered password is not a Valid Password")

    return


if __name__ == "__main__":
    main()