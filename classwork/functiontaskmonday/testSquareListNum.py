import unittest
import SquareListNum


class FunctionThatSquaresTheListOfNum(unittest.TestCase):
	def test_that_fuction_square_list_num_exist(self):
		SquareListNum.square_num([1,4,9,16])
	def test_that_fuction_returns_correct_value(self):
		SquareListNum.square_num([1,4,9,16])
	def test_that_function_doest_accept_negetive_input(self):
		self.assertRaises(TypeError,SquareListNum.square_num,"Edwin")		
		