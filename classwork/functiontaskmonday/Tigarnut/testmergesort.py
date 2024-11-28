import unittest
import Mergesort

class TestMergeSortFunction(unittest.TestCase):
	def test_that_function_merge_sort_exists(self):
		Mergesort.merge_sort([3,4,9,10],[1,5,7,8])

	def test_that_function_merge_sort_returns_correct_value(self):
		actual = Mergesort.merge_sort([3,4,9,10],[1,5,7,8])
		expected = [1,3,4,5,7,8,9,10]	
		self.assertEqual(actual,expected)

	def test_that_function_merge_sort_raises_exception_with_invalid_input(self):
		self.assertRaises(TypeError,Mergesort.merge_sort,"Edwin")	
	