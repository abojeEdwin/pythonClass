import unittest
import sumEven


class FunctionTestForSumEvenNum(unittest.TestCase):
	def test_that_function_sum_even_num_exist(self):
		sumEven.sumEven_num([2,7,9,17,19,2,8,10])
	