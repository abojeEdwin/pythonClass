import unittest
import functionSum


class FunctionSumForList(unittest.TestCase):



	def test_that_function_sum_exists(self):
		functionSum.get_sum(1,2,3)
	def test_that_function_sum_returns_int(self):
		actual = functionSum.get_sum(2,3,4)
		expected = 9
		self.assertEqual(actual,expected)
	def test_that_function_sum_recieves_list_of_number(self):
		actual = functionSum.get_sum(2,3,4)
		expected = 9
		self.assertEqual(actual,expected)












