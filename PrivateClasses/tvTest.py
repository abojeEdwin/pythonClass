import unittest
from Television import Tv


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tv = Tv()

    def test_that_tv_isOn(self):
        self.tv.turnOn()
        self.assertTrue(self.tv.is_On_status())

    def test_that_tv_isOff(self):
        self.tv.turnOff()
        self.assertFalse(self.tv.is_On_status())

    def test_that_tv_can_increase_volume(self):
        self.tv.turnOn()
        self.tv.increaseVolume()
        self.tv.increaseVolume()
        self.tv.increaseVolume()
        self.tv.increaseVolume()
        self.tv.increaseVolume()
        self.tv.increaseVolume()
        self.tv.increaseVolume()
        self.tv.increaseVolume()
        self.assertEqual(8, self.tv.getvolumeLevel())

    def test_that_tv_can_decrease_volume(self):
        self.tv.turnOn()
        self.tv.increaseVolume()
        self.tv.increaseVolume()
        self.tv.increaseVolume()
        self.tv.decreaseVolume()
        self.assertEqual(2, self.tv.getvolumeLevel())

    def test_that_tv_can_change_channel_down(self):
        self.tv.turnOff()
        self.tv.channelDown()
        self.tv.channelDown()
        self.tv.channelDown()
        self.tv.channelDown()
        self.assertEqual(0,self.tv.getchannelLevel() )

    def test_that_tv_can_change_channel_up(self):
        self.tv.channelUp()
        self.tv.channelUp()
        self.tv.channelUp()
        self.tv.channelDown()
        self.assertEqual(2, self.tv.getchannelLevel())

    def test_that_tv_can_set_channel(self):
        self.tv.setChannel(7)
        actual = self.tv.getChannel()
        expected = 7
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
