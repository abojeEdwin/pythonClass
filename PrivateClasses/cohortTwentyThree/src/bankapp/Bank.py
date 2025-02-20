from cohortTwentyThree.src.bankapp.Account import *


class MyBank:
    def __init__(self):
        self.__accounts = []
        self.__account_number = 0

    def createAccount(self, first_name, password):
        self.__account_number += 1
        self.__accounts.append(MyAccount(first_name,self.__account_number,password))
        return self.__accounts[-1]


    def transfer(self,sender_account,recievers_account,amount,password):
        reciever = self.find_account_by_accountnumber(recievers_account).deposit(amount)
        sender_account = self.find_account_by_accountnumber(sender_account).withdraw(amount,password)
        if self.find_account_by_accountnumber(recievers_account) == self.find_account_by_accountnumber(sender_account):
            raise IndexError("Account cannot be the same")


    def withdraw(self,accountnumber,amount,password):
        accountnumber = self.find_account_by_accountnumber(accountnumber)
        accountnumber.withdraw(amount,password)

    def deposit(self,accountnumber,amount):
        accountnumber = self.find_account_by_accountnumber(accountnumber)
        accountnumber.deposit(amount)


    def find_account_by_accountnumber(self, account_number):
        if account_number is None : return IndexError("Account number not found")
        for account in self.__accounts:
          if account.get_account_number() == account_number:
              return account


    def get_account_number(self):
        return self.__account_number

    def get_balance(self,accountnumber,password):
        accountnumber = self.find_account_by_accountnumber(accountnumber)
        return accountnumber.checkBalance(password)

