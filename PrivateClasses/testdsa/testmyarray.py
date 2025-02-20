import unittest
from dsa.myarray import MyArray

class MyTestCase(unittest.TestCase):
    def test_that_my_array_can_add(self):
        my_array = MyArray(10)
        my_array.add(9)
        my_array.add(8)
        my_array.add(7)
        self.assertEqual(3,my_array.getSize())

    def test_that_my_array_remove(self):
        my_array = MyArray(10)
        my_array.add(9)
        my_array.add(8)
        my_array.remove()
        self.assertEqual(1,my_array.getSize())

    def test_that_my_array_contains_an_item(self):
        my_array = MyArray(10)
        my_array.add(9)
        my_array.add(8)
        self.assertTrue(my_array.isContain(9))
        self.assertFalse(my_array.isContain(100))

    def test_that_my_array_returns_correct_size(self):
        my_array = MyArray(10)
        self.assertEqual(10,my_array.getCapacity())

    def test_that_my_array_is_empty(self):
        my_array = MyArray(10)
        self.assertTrue(my_array.isEmpty())

    def test_that_my_array_handles_exception_when_full(self):
        my_array = MyArray(5)
        my_array.add(200)
        my_array.add(10)
        my_array.add(20)
        my_array.add(220)
        my_array.add(50)
        self.assertRaises(IndexError,my_array.add, 21)

    def test_that_my_array_is_handels_expection_when_trying_to_remove_from_an_empty_array(self):
        my_array = MyArray(5)
        self.assertRaises(ValueError,my_array.remove)


if __name__ == '__main__':
    unittest.main()
