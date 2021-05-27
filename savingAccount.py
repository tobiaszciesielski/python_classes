from account import Account


class SavingsAccount(Account):
    interest_rate = 0.01

    def calc_interest(self):
        self._balance += self.interest_rate * self._balance

    def __repr__(self):
      return 'SavingAccount[{},{},{}]'.format(self.id, self.customer.lastname, self._balance)
