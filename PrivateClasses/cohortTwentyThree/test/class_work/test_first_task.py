import unittest
from cohortTwentyThree.test.class_work import first_task
from cohortTwentyThree.test.class_work.upper_case import mixed_case
from cohortTwentyThree.test.class_work.remove_special_characters import remove_special_characters
from cohortTwentyThree.test.class_work.secondTask import swap_letters
from cohortTwentyThree.test.class_work.thirdTask import find_middle
from cohortTwentyThree.test.class_work.first_task import first_task
from cohortTwentyThree.test.class_work.occurance import return_occurance

class MyTestCase(unittest.TestCase):
    def test_that_remove_special_characters_returns_correct_values(self):
        actual = remove_special_characters("se,mi,co,lon")
        expected = "semicolon"
        self.assertEqual(actual,expected)

    def test_that_upper_case_function_works(self):
        actual = mixed_case("sEmIColOn")
        expected = "EICOsmoln"
        self.assertEqual(actual,expected)

    def test_that_swap_letters_works(self):
        actual = swap_letters("abc","xyz")
        expected = "xyc abz"
        self.assertEqual(actual,expected)

    def test_that_find_middle_returns_correct_value(self):
        actual = find_middle("helllo","ce")
        expected = "helcello"
        self.assertEqual(actual,expected)

    def test_that_first_task_returns_correct_value(self):
        actual = first_task('semicolon.africa')
        expected =  {'s':1,'e':1,'m':1,'i':2,'c':2,'o':2,'l':1,'n':1,'.':1,'a':2,'f':1,'r':1}
        self.assertEqual(actual,expected)

    def test_that_return_occurance_returns_correct_value(self):
        actual= return_occurance("semicolon","o")
        expected = ('o',2)
        self.assertEqual(actual,expected)


if __name__ == '__main__':
    unittest.main()
