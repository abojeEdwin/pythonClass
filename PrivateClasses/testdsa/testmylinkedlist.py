import unittest
from dsa.linkedlist import MyLinkedList


class MyTestCase(unittest.TestCase):
    def test_that_my_linkedlist_can_insert_items(self):
        linkedlist = MyLinkedList()
        linkedlist.insert(9)
        linkedlist.insert(20)
        self.assertEqual(2,linkedlist.getSize())

    def test_that_my_linkedlist_can_remove_items(self):
        linkedlist = MyLinkedList()
        linkedlist.insert(9)
        linkedlist.insert(20)
        linkedlist.removeAt(0)
        self.assertEqual(1,linkedlist.getSize())



if __name__ == '__main__':
    unittest.main()
