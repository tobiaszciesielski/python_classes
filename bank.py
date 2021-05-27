from errors import BankException
from account import Account
from savingAccount import SavingsAccount
from checkingAccount import CheckingAccount
from customer import Customer


class Bank:
    customers = []
    accounts = []

    def new_customer(self, first_name, last_name):
        customer = Customer(first_name, last_name)
        self.customers.append(customer)
        return customer

    def create_account(self, accountType, customer):
        account = accountType(customer)
        self.accounts.append(account)
        return account

    def transfer(self, from_acc_id, to_acc_id, amount):
        account_from = self.find_account_by_id(from_acc_id)
        account_to = self.find_account_by_id(to_acc_id)
        account_from.charge(amount)
        account_to.deposit(amount)


    def find_account_by_id(self, acc_id):
        for index, account in enumerate(self.accounts):
            if account.id == acc_id:
                return self.accounts[index]

        raise BankException("Account with provided id not found")
