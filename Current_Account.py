from Account import Account


class Current_Account(Account):
    """"Class inheriting from the Account class"""
    overdraft: int
    agios_percentage: int


    def apply_agios(self):
        amount = 0
        return amount
