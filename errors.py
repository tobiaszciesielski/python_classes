class BankException(Exception):
    pass


class NegativeAmountException(BankException):
    pass


class NotEnoughBalanceException(BankException):
    pass

  
