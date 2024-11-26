import unittest
import SwitchList


class TestFucntionGetSwitchList(unittest.TestCase):
	def test_that_get_switch_list_exist(self):
		SwitchList.getSwitchList([1,2,3,4,5],3)

	def test_that_get_switch_list_return_correct_value(self):
		expected = SwitchList.getSwitchList([1,2,3,4,5],3)
		actual = [4,5,1,2,3]
		self.assertEqual(actual,expected)