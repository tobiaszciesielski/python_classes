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
        account_from = None
        account_to = None 

        for index, account in enumerate(self.accounts):
            if account.id == from_acc_id:
                account_from = self.accounts[index]
            if account.id == to_acc_id:
                account_to = self.accounts[index]

        if account_to == None or account_from == None:
            raise BankException("Account with provided id not found")

        account_from.charge(amount)
        account_to.deposit(amount)
