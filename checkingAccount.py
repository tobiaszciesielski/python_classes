from account import Account

class CheckingAccount(Account):
    def __repr__(self):
      return 'CheckingAccount[{},{},{}]'.format(self.id, self.customer.lastname, self._balance)
