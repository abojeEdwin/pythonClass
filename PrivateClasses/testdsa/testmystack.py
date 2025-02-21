import unittest
from dsa.mystack import MyStack

class MyTestCase(unittest.TestCase):
    def setUp(self):
        stack = MyStack(6)

    def test_that_my_stack_is_empty(self):
        stack = MyStack(6)
        stack.push(1)
        self.assertFalse(stack.isEmpty())


    def test_that_my_stack_can_add_items(self):
        stack = MyStack(6)
        stack.push(1)
        stack.push(2)
        self.assertEqual(2,stack.getSize())

    def test_that_my_stack_can_remove(self):
        stack = MyStack(6)
        stack.push(1)
        stack.push(2)
        stack.push(15)
        stack.pop()
        stack.pop()
        self.assertEqual(1,stack.getSize())


    def test_that_my_stack_can_peek(self):
        stack = MyStack(6)
        stack.push(290)
        stack.push(67)
        stack.push("Here we go")
        stack.peek()


if __name__ == '__main__':
    unittest.main()
