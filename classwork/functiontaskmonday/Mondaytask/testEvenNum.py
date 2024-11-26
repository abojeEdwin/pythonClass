import unittest
import EvenNumList


class TestEvenNumChecksEven(unittest.TestCase):
	def test_that_get_even_num_list_exist(self):
		EvenNumList.getNumList(1,4,3,2,5,9)