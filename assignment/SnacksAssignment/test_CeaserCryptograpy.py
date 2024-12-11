import unittest
from CeaserCryptography import *


class TestCaeserCryptographyFunction(unittest.TestCase):
	def test_that_ceaser_cryptography_encrypted_exist(self):
		ceaser_CryptographyEncrypted("message" ,3)

	def test_that_ceaser_cryptography_encrypted_returns_correct_value(self):
		actual = ceaser_CryptographyEncrypted("Edwin", 3)
		expected =" Hgzlq"
		self.assertEqual(actual, expected)


class TestCaeserCryptographyDecryptFunction(unittest.TestCase):
	def test_that_caeser_cryptography_decrypted_exist(self):
		ceaser_CryptograpyDecrypted("Edwin", 3)

	def test_that_caeser_cryptography_decrypted_returns_correct_value(self):
		actual = ceaser_CryptograpyDecrypted("Hgzlq", 3)
		expected = " Edwin"
		self.assertEqual(actual, expected)