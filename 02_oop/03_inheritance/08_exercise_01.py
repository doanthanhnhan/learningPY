"""
Implement a Banking Account
+ Implement properties as instance variables and set them to None or 0.
Account has the following properties:

title
balance
SavingsAccount has the following properties:

interestRate

+ Create an initializer for Account class.
+ Implement properties as instance variables and set them to None or 0.
"""


class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
