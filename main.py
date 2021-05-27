from savingAccount import SavingsAccount
from checkingAccount import CheckingAccount
from bank import Bank
from customer import Customer

bank = Bank()
c1 = bank.new_customer('tobi', 'cie')
c2 = bank.new_customer('jakub', 'pawl')
ac1 = bank.create_account(CheckingAccount, c1)
ac2 = bank.create_account(SavingsAccount, c2)

ac1.deposit(300)

bank.transfer(ac1.id, ac2.id, 200)
