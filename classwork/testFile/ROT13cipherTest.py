import unittest
from classwork.ROT13cipher import encrypt_text


class ROTcipher(unittest.TestCase):

    def test_function_encrypttext_Exist(self):
        encrypt_text("Hello World")

    def test_function_encrpttext_returns_correct_text(self):
        expected = "Uryyb,Jbeyq!"
        actual = encrypt_text("Hello,World!")
        self.assertEqual(expected, actual)

    def test_function_encrypt_returns_correct_text(self):
        expected = "jrypbzr,123"
        actual = encrypt_text("welcome,123")
        self.assertEqual(expected, actual)







if __name__ == '__main__':
    unittest.main()