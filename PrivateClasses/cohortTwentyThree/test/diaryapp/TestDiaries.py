import unittest
from cohortTwentyThree.src.diaryapp.Diaries import Diaries
from cohortTwentyThree.src.diaryapp.Diary import Diary


class MyTestCase(unittest.TestCase):
    def test_that_Diaries_class_can_create_new_diaries(self):
        diaries = Diaries()

    def test_that_Diaries_class_can_create_a_new_diary_and_add_new_entry(self):
        diary = Diary("Edwin", "1234","1")
        diary.createEntry("my little secret","today is not just another day")
        self.assertEqual(1,diary.getSize())

    def test_that_diary_is_locked(self):
        diary = Diary("Edwin", "1234",1)
        self.assertFalse(diary.isLocked())

    def test_that_dairy_can_be_locked(self):
        diary = Diary("Edwin", "1234",1)
        diary.createEntry("my little secret", "today is not just another day")
        diary.lock()
        self.assertTrue(diary.isLocked())

    def test_that_diary_can_be_unlocked(self):
        diary = Diary("Edwin", "1234",1)
        diary.createEntry("my little secret", "today is not just another day")
        diary.lock()
        self.assertTrue(diary.isLocked())
        diary.unlock("1234")
        self.assertFalse(diary.isLocked())

    def test_that_dairy_handles_exceptions_when_trying_to_unlock(self):
        diary = Diary("Edwin", "1234",1)
        diary.createEntry("my little secret", "today is not just another day")
        diary.lock()
        self.assertRaises(ValueError,diary.unlock("34567"))

    def test_that_diary_can_delete_entry_by_id(self):
        diary = Diary("Edwin","12345",1)
        diary.createEntry("my little secret","today is not just another day")
        diary.createEntry("here we go","today is not just another day")
        diary.deleteEntryById(1)
        self.assertEqual(1,diary.getSize())


    def test_that_diary_can_update_entry_by_id(self):
        diary = Diary("Edwin","12345",1)
        diary.createEntry("my little secret","today is not just another day")
        diary.update("it is no longer a secret","Today is still not just another day",1)
        self.assertEqual(1,diary.getSize())


    def test_that_diary_cannot_add_entry_when_locked(self):
        diary = Diary("Edwin","12345",1)
        diary.lock()
        self.assertTrue(diary.isLocked())
        self.assertRaises(ValueError,diary.createEntry("my little secret","today is not just another day"))

    def test_that_diary_handles_exceptions_when_creating_a_new_diary(self):
        self.assertRaises(TypeError,Diary(None," ",0))




if __name__ == '__main__':
    unittest.main()
