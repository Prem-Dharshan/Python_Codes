# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 09:13:10 2023

@author: 22pw29
"""

"""5. ABC Bank updates its customers’ accounts at the end of each month. The bank offers two
types of accounts: savings and checking. Every customer must maintain a minimum
balance 1000 for savings account and 5000 for checking account. If a customer’s balance
falls below the minimum balance, there is a service charge of Rs. 500 for savings account

and RS.1500 for checking account. Also, If the balance at the end of the month is at least
the minimum balance, then the account receives interest as follows:
 Savings account receives 4% interest
 Checking account with balance of up to RS. 250000 receive 3% interest; an account
with balance greater than 250000 receives 5% interest.
Write a program that reads a customer’s account number (int type), account type(char;
s for savings, c for checking), and current balance. The program should then output the
account number, account type, current balance, and an appropriate message."""

class Account:

    acctNum: int
    acctType: str
    balance: int
        
        
    def __init__(self, acctNum: int, accType: str, balance: int):
        self.acctNum = acctNum
        self.acctType = accType
        self.balance = balance

    def isValid(self):
        if self.acctType == 's':
            return self.balance >= 1000
        elif self.acctType == 'c':
            return self.balance >= 5000
        else:
            return False

    def getInterestRate(self):
        if self.acctType == 's':
            return 0.04
        elif self.acctType == 'c' and self.balance <= 250000:
            return 0.03
        elif self.acctType == 'c' and self.balance > 250000:
            return 0.05
        else:
            return 0

    def MonthlyChanges(self):
        if not self.isValid():
            if self.acctType == 's':
                self.balance -= 500
            elif self.acctType == 'c':
                self.balance -= 1500
        else:
            interestRate = self.getInterestRate()
            interest = self.balance * interestRate
            self.balance += interest

        return self.balance


def main():
    acctNum = int(input("Enter account number: "))
    acctType = input("Enter account type (s for savings, c for checking): ")
    balance = float(input("Enter current balance: "))

    account = Account(acctNum, acctType, balance)
    newBal = account.MonthlyChanges()

    print(f"Account number: {account.acctNum}")
    print(f"Account type: {account.acctType}")
    print(f"Current balance: {account.balance:.2f}")

    if account.isValid():
        print("Account is valid and no charges have been applied.")
    else:
        if account.acctType == 's':
            print("Account has fallen below the minimum balance of 1000. A service charge of 500 has been applied.")
        elif account.acctType == 'c':
            print("Account has fallen below the minimum balance of 5000. A service charge of 1500 has been applied.")

    print(f"New balance: {newBal:.2f}")


if __name__ == '__main__':
    main()
