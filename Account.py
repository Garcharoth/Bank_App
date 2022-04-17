import string
from abc import ABC


class Account(ABC):
    """This is an abstract class"""
    account_number: int
    account_holder: string
    balance: float

    def __init__(self, account_number: int, account_holder: string, balance: float):
        self.__account_number: account_number
        self.__account_holder: account_holder
        self.__balance = balance

    def withdraw(self, amount):
        new_balance = self.balance - amount
        if new_balance < -100:
            return print(f"Attention, plafond de découvert atteint, Agios applicables ! Nouveau solde : %i Euros " %new_balance )
        elif new_balance > -100:
            return print(f"Nouveau solde : %i Euros" %new_balance)

    def deposit(self, amount):
        self.balance += amount
        return print(f"Le nouveau solde est de : %i Euros" %self.balance)

    def show_balance(self):
        return print(f"Votre solde est de : %i Euros" %self.balance)

