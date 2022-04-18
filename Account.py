from abc import ABC


class Account(ABC):
    """This is an abstract class representing the basic account"""
    account_number: int
    account_holder: str
    balance: float

##### CONSTRUCTOR ######

    def __init__(self, account_number: int, account_holder: str, balance: float):
        """Constructeur de la classe account"""
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance


##### GETTER & SETTERS #####

    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    def set_account_number(self, new_number):
        self.__account_number = new_number

    def set_account_holder(self, new_name):
        self.__account_holder = new_name

    def set_balance(self, new_balance):
        self.__balance = new_balance


##### STR #####
    def __str__(self):
        return "Je suis un compte"


    def show(self):
        print("======")
        print("Nom : ", self.get_account_holder(), "solde : ", self.get_balance())
        print("======")

##### METHODS #####

    def withdraw(self, amount):
        """withdraw money and update balance"""
        new_balance = self.get_balance() - amount
        self.set_balance(new_balance)


    def deposit(self, amount):
        self.__balance += amount
        return print(f"Le nouveau solde est de : %i Euros" %self.__balance)

    def show_balance(self):
        return print(f"Votre solde est de : %i Euros" %self.__balance)

