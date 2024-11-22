import unittest
import cornflake
import math


class TestDivideSquareFunction(unittest.TestCase):

	def test_that_function_corn_flake_exists(self):
		cornflake.divide_or_square(10)

	def test_that_function_corn_flake_doesnt_take_string(self):
		self.assertRaises(TypeError,cornflake.divide_or_square, "Edwin")

	def test_that_function_corn_flake_doesnt_take_negetive_input(self):
		actual = cornflake.divide_or_square(-10)
		expected = "valid input" 
		self.assertEqual(actual,expected)

	def test_that_function_doesnt_take_invalid_character(self):
		self.assertRaises(TypeError,cornflake.divide_or_square, "@")

	def test_that_function_corn_flake_if_mod_number_not_equal_to_zero(self):
		actual = cornflake.divide_or_square(14)
		expected = 4

	def test_that_function_corn_flake_mod_square_rounds_to_two_decimal(self):
		actual = cornflake.divide_or_square(round(math.sqrt(10),2))
		expected = 3.16
		


#another test for investment amount#




class TestFutureInvestmentAmount(unittest.TestCase):
	def test_that_function_corn_flake_exists(self):
		cornflake.future_investment_amount(1,2,3)
		
	def test_that_function_corn_flakes_holds_three_arguments(self):
		self.assertEqual("PositionalError",cornflake.future_investment_amount("PositionalError"))
	























if __name__ == ("__main__"):
	unittest.main()