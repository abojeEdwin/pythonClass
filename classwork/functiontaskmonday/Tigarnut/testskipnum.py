import unittest
import Skipsum


class TestFunctionSkipSumation(unittest.TestCase):
	def test_that_skip_sum_exist(self):
		Skipsum.skip_sum([1,2,3,4,5])
	def test_that_skip_sum_returns_correct_value(self):
		actual = Skipsum.skip_sum([1,2,3,4,5])
		expected = 50
		self.assertEqual(actual,expected)
		