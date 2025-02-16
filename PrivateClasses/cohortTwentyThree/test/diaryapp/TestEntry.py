import unittest
from cohortTwentyThree.src.diaryapp.Entry import Entry

class MyTestCase(unittest.TestCase):
    def test_That_entry_class_can_get_ID(self):
        entry = Entry("0","Today is not just another day","My little secret")
        self.assertEqual("0",entry.getId())

    def test_that_entry_class_can_get_title(self):
        entry = Entry("0","Today is not just another day","My little secret")
        self.assertEqual("Today is not just another day", entry.getTitle())

    def test_that_entry_class_can_get_body(self):
        entry = Entry("0","Today is not just another day","My little secret")
        self.assertEqual("My little secret",entry.getBody())


















if __name__ == '__main__':
    unittest.main()
