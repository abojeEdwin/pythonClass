import unittest
import Tv


class MyTestCase(unittest.TestCase):
    def test_that_Tv_isOn(self):
        actual = Tv.isOn()
        expected = False
        self.assertFalse(actual, expected)

    def test_that_Tv_isOff(self):
        actual = Tv.turnOff()
        expected = True
        self.assertEqual(actual, expected)

    def test_that_Tv_can_turn_on(self):
        actual1 = Tv.turnOn()
        actual2 = Tv.turnOff()
        actual3 = Tv.turnOn()
        expected = True
        self.assertFalse(actual3, expected)

    def test_that_Tv_can_IncreaseVolume(self):
        actual = Tv.increaseVolume(self)
        expected = 1
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
