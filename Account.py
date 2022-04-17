import string
from abc import ABC


class Account(ABC):
    """This is an abstract class"""
    account_number: int
    account_holder: string
    balance: int


    def withdraw(self):
        amount = 0
        return amount

    def payment(self):
        amount=0
        return amount

    def show_balance(self):
        return print(self.balance)

