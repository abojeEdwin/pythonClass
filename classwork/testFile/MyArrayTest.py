import unittest
from classwork import MyArray


class TestMyArrayFunctions(unittest.TestCase):


    def test_that_my_array_class_isEmpty(self):
        MyArray.isEmpty()


    def test_that_my_array_class_can_add_items(self):
        expected = 3
        actual = MyArray.addItem("G String"),MyArray.addItem("B String"),MyArray.addItem("C String")
        self.assertTrue(3, MyArray.size())

    def test_that_my_array_function_can_remove_items(self):
        MyArray.addItem("G String")
        expected = 0
        actual = MyArray.removeItem("G String")
        self.assertEqual(expected, actual)












if __name__ == '__main__':
    unittest.main()
