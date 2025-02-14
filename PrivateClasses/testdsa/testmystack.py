import unittest
from dsa.mystack import MyStack

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = MyStack(6)

    def test_that_my_stack_is_empty(self):
        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty())


    def test_that_my_stack_can_add_items(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(2,self.stack.getSize())

if __name__ == '__main__':
    unittest.main()
