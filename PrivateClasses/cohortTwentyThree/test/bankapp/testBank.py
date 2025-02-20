import unittest
from cohortTwentyThree.src.bankapp.Bank import *

class MyTestCase(unittest.TestCase):
    def test_that_bank_can_create_account(self):
        bank = MyBank()
        account = bank.createAccount("Edwin aboje","12345")
        self.assertEqual(1,bank.find_account_by_accountnumber(1).get_account_number())

    def test_that_bank_can_initiate_a_transfer(self):
        bank = MyBank()
        account = bank.createAccount("Edwin aboje","12345")
        self.assertEqual(1,bank.find_account_by_accountnumber(1).get_account_number())
        bank.deposit(1,5000)
        self.assertEqual(5000,account.checkBalance("12345"))
        account2 =  bank.createAccount("Sam Immanuel","23456")
        self.assertEqual(2,bank.find_account_by_accountnumber(2).get_account_number())
        bank.transfer(1 ,2,3000,"12345")
        self.assertEqual(3000,bank.get_balance(2,"23456"))

    def test_that_bank_can_withdraw(self):
        bank = MyBank()
        account =  bank.createAccount("Edwin aboje","12345")
        bank.deposit(1,5000)
        bank.withdraw(1,4500,"12345")
        self.assertEqual(500,bank.get_balance(1,"12345"))





if __name__ == '__main__':
    unittest.main()
