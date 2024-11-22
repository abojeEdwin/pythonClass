import unittest
import test_multiplefunction

class TestMultipleFunction(unittest.TestCase):
	def test_that_function_multiple_exists(self):
		test_multiplefunction.get_multiple(3,3)