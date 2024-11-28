import unittest
import Sumfunction


class TestEvenSumFunction(unittest.TestCase):
	def test_that_get_sum_function_exist(self):
		Sumfunction.get_sum_func(1,2,3,4)

	def test_that_get_sum_function_takes_a_list(self):
		Sumfunction.get_sum_func(numbers)
		actual = 1,2,3,4
		expected = 6
		self.assertEqual(actual,expected(6))