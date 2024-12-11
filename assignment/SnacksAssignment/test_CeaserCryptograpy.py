import unittest
from CeaserCryptography import *


class TestCaeserCryptographyFunction(unittest.TestCase):
	def test_that_ceaser_cryptography_encrypted_exist(self):
		ceaser_CryptographyEncrypted("message" ,3)

	def test_that_ceaser_cryptography_encrypted_returns_correct_value(self):
		actual = ceaser_CryptographyEncrypted("Edwin", 3)
		expected =" Hgzlq"
		self.assertEqual(actual, expected)