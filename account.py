from errors import NegativeAmountException, NotEnoughBalanceException


class Account:
    last_id = 0

    def __init__(self, customer):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print('New deposit updated as: ' + str(self._balance))
        else:
            print('The amount is negative')

    def charge(self, amount):
        if amount > self._balance:
            raise NotEnoughBalanceException(
                "You don't have enough Balance. Your Current Balance is " + str(self._balance))
        if amount <= 0:
            raise NegativeAmountException(
                "The amount is negative. Please input the positive amount")
        else:
            self._balance -= amount
            print("Charge amount from " + str(self.id) + ": " + str(amount))
            print("New Balance updated as: " + str(self._balance))

