import unittest
import functionbestperforming

class FunctionTestForBestPerforming(unittest.TestCase):
	def test_that_get_best_performing_exists(self):
		functionbestperforming.get_best_performing([20,30,40,50,60])
			