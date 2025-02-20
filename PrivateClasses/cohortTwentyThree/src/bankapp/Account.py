class MyAccount:
    def __init__(self, name,account_number,password):
        self.__name = name
        self.__balance = 0
        self.__password = password
        self.__account_number = account_number

    def deposit(self, amount):
        self.__balance += amount


    def checkBalance(self,password):
        if self.__password != password:
            raise ValueError("Password does not match")
        return self.__balance

    def withdraw(self, amount,password):
        if amount is " ":
            raise ValueError("Amount cannot be empty")
        if amount is None:
            raise ValueError("Amount cannot be None")
        if self.__balance <= amount:
            raise IndexError("Not enough money")
        if self.__password != password:
            raise ValueError("Password does not match")
        self.__balance -= amount

    def updatePassword(self,oldPassword,newPassword):
        if oldPassword is not self.__password:
            raise ValueError("Password does not match")
        self.__password = newPassword

    def getName(self):
        if self.__name is None or self.__name is " ":
            raise ValueError("Name cannot be empty")
        return self.__name

    def get_account_number(self):
        return self.__account_number


