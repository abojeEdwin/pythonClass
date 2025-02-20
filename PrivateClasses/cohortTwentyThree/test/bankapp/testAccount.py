import unittest
from cohortTwentyThree.src.bankapp.Account import MyAccount

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.account  = MyAccount("Aboje Edwin","1","12345")


    def test_that_Account_class_can_deposit(self):
        account = MyAccount("Aboje Edwin","1","12345")
        account.deposit(5000)
        self.assertEqual(5000,account.checkBalance("12345"))

    def test_that_Account_class_does_not_check_balance_if_password_isInvalid(self):
        account = MyAccount("Aboje Edwin","1","12345")
        self.assertRaises(ValueError,account.checkBalance,"34563")

    def test_that_Account_class_can_withdraw(self):
        account = MyAccount("Aboje Edwin","1","12345")
        account.deposit(5000)
        account.withdraw(2000,"12345")
        self.assertEqual(3000,account.checkBalance("12345"))

    def test_that_Account_class_does_not_withdraw_when_empty(self):
        account = MyAccount("Aboje Edwin", "1", "12345")
        self.assertRaises(IndexError,account.withdraw,2000)

    def test_that_Account_class_handles_error_when_withdraw_amount_is_none(self):
        account = MyAccount("Aboje Edwin", "1", "12345")
        self.assertRaises(ValueError,account.withdraw,None)


    def test_that_Account_class_handles_error_when_withdraw_amount_with_empty_string(self):
        account = MyAccount("Aboje Edwin", "1", "12345")
        self.assertRaises(ValueError,account.withdraw," ")

    def test_that_Account_class_can_change_pin(self):
        account = MyAccount("Aboje Edwin", "1", "12345")
        account.updatePassword("12345","09876")
        account.deposit(2000)
        account.withdraw(1000,"09876")
        self.assertEqual(1000,account.checkBalance("09876"))

    def test_that_account_class_can_get_name(self):
        account = MyAccount("Aboje Edwin", "1", "12345")
        self.assertEqual("Aboje Edwin",account.getName())


if __name__ == '__main__':
    unittest.main()