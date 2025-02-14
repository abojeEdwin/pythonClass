import unittest
from dsa.myqueue import MyQueue


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.queue = MyQueue(5)

    def test_that_my_queue_is_empty(self):
        self.queue.enterQueue(15)
        self.assertFalse(self.queue.isEmpty())

    def test_that_my_queue_can_add_item(self):
        self.queue.enterQueue(15)
        self.queue.enterQueue(21)
        self.queue.enterQueue(1)
        self.assertEqual(3,self.queue.getSize())

    def test_that_queue_can_display_items_in_it(self):
        self.queue.enterQueue(15)
        self.queue.enterQueue(21)
        self.queue.enterQueue(1)
        self.queue.show()

    def test_that_queue_can_remove_item(self):
        self.queue.enterQueue(15)
        self.queue.enterQueue(21)
        self.queue.enterQueue(1)
        self.queue.remove()
        self.assertEqual(2,self.queue.getSize())

    def test_that_queue_is_full(self):
        self.queue.enterQueue(15)
        self.queue.enterQueue(21)
        self.queue.enterQueue(1)
        self.queue.enterQueue(15)
        self.queue.enterQueue(21)
        self.queue.enterQueue(1)
        with self.assertRaises(IndexError):
            (self.queue.isFull())


    def test_that_queue_can_only_remove_if_empty(self):
       self.queue.remove()







if __name__ == '__main__':
    unittest.main()
