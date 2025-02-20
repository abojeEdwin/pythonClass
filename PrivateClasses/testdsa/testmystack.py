import unittest
from dsa.mystack import MyStack

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = MyStack(6)

    def test_that_my_stack_is_empty(self):
        stack = MyStack(6)
        stack.push(1)
        self.assertFalse(self.stack.isEmpty())


    def test_that_my_stack_can_add_items(self):
        stack = MyStack(6)
        stack.push(1)
        stack.push(2)
        self.assertEqual(2,self.stack.getSize())

    def test_that_my_stack_can_remove(self):
        stack = MyStack(6)
        stack.push(1)
        stack.push(2)
        stack.push(15)
        stack.pop()
        self.assertEqual(2,self.stack.getSize())


    def test_that_my_stack_can_display(self):
        stack = MyStack(6)
        stack.push(20)
        stack.push(22)
        stack.display()


if __name__ == '__main__':
    unittest.main()
