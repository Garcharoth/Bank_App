from Account import Account


class SavingsAccount(Account):
    interests_percentage: float

    ##### CONSTRUCTOR #####
    def __init__(self, account_number: int, account_holder: str, balance: float, interests_percentage: int):
        super().__init__(account_number, account_holder, balance)
        self.__interests_percentage = interests_percentage


    ##### GETTERS AND SETTERS #####

    def get_interests(self):
        return self.__interests_percentage

    def set_interests(self, new_interests):
        self.__interests_percentage = new_interests


    ##### METHODS #####

    def withdraw(self, amount):
        print("Withdraw saving account")
        new_balance = self.get_balance() - amount
        if new_balance >= 0:
            self.set_balance(new_balance)
        elif new_balance < 0:
            print("Le nouveau montant serait inférieur a 0, retrait non autorise")


    def deposit(self, amount):
        interests = self.apply_interests(amount)
        new_balance_interests = self.get_balance() + amount + interests
        self.set_balance(new_balance_interests)


    def apply_interests(self, amount):
        applied_interests = amount * self.get_interests()/100
        return applied_interests
