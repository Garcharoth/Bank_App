from Account import Account


class CurrentAccount(Account):
    """"Class inheriting from the Account class"""
    overdraft: int
    agios_percentage: float


##### CONSTRUCTOR ######
    def __init__(self, account_number: int, account_holder: str, balance: float, overdraft: int, agios_percentage: float):
        super().__init__(account_number, account_holder, balance)
        self.__overdraft = overdraft
        self.__agios_percentage = agios_percentage


##### GETTERS AND SETTERS #####

    def get_overdraft(self):
        return self.__overdraft

    def get_agios_percentage(self):
        return self.__agios_percentage

    def set_overdraft(self, new_overdraft):
        self.__overdraft = new_overdraft

    def set_agios_percentage(self, new_agios):
        self.__agios_percentage = new_agios



##### METHODS #####
    def withdraw(self, amount):
        """méthode pour retirer de l'argent, le compte n'est pas bloqué
        mais a 'overdraft' de un découvert autorisé avant d'appliquer les agios (de -100 a -infinite)"""
        print("Withdraw current account")
        new_balance = self.get_balance() - amount
        if new_balance >= self.get_overdraft():
            self.set_balance(new_balance)
        elif new_balance < self.get_overdraft():
            #print("on calcule les agios")
            agios = self.apply_agios(amount)
            #print("on soustrait les agios a new balance")
            new_balance_agios = self.get_balance() - amount - agios
            #print("on set le nouveau solde en fonction des agios")
            self.set_balance(new_balance_agios)



    def apply_agios(self, amount):
        """les agios s'appliquent sur le montant retire"""
        applied_agios = amount * self.get_agios_percentage()/100
        return applied_agios
