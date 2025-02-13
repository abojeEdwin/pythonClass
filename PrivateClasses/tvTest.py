import unittest
from Television import Tv


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tv = Tv()

    def test_that_tv_is_off(self):
        self.assertFalse(self.tv.is_On_status())

    def test_that_tv_can_come_on(self):
        self.assertFalse(self.tv.is_On_status())
        self.tv.turnOn()
        self.assertTrue(self.tv.is_On_status())

    def test_that_tv_can_go_off(self):
        self.tv.turnOn()
        self.assertTrue(self.tv.is_On_status())
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
        self.tv.decreaseVolume()
        self.assertEqual(1, self.tv.getvolumeLevel())

    def test_that_tv_can_change_channel_up(self):
        self.tv.turnOn()
        self.tv.channelUp()
        self.tv.channelUp()
        self.tv.channelUp()
        self.tv.channelUp()
        self.assertEqual(4,self.tv.getchannelLevel() )

    def test_that_tv_can_change_channel_down(self):
        self.tv.turnOn()
        self.tv.channelUp()
        self.tv.channelUp()
        self.tv.channelUp()
        self.tv.channelDown()
        self.tv.channelDown()
        self.assertEqual(1, self.tv.getchannelLevel())

    def test_that_tv_can_set_channel(self):
        self.tv.turnOn()
        self.tv.setChannel(7)
        self.assertEqual(7,self.tv.getChannel())

    def test_that_tv_can_mute(self):
        self.tv.turnOn()
        self.tv.increaseVolume()
        self.tv.increaseVolume()
        self.tv.increaseVolume()
        self.assertEqual(3, self.tv.getvolumeLevel())
        self.tv.mute()
        self.assertEqual(0,self.tv.getvolumeLevel())

    def test_that_tv_can_unmute(self):
        self.tv.turnOn()
        self.tv.increaseVolume()
        self.tv.increaseVolume()
        self.assertEqual(2,self.tv.getvolumeLevel())
        self.tv.mute()
        self.assertEqual(0,self.tv.getvolumeLevel())
        self.tv.unmute()
        self.assertEqual(2,self.tv.getvolumeLevel())

    def test_that_television_does_not_increase_volume_when_off(self):
        self.tv.increaseVolume()
        self.tv.increaseVolume()
        self.assertEqual(0,self.tv.getvolumeLevel())

    def test_that_television_does_not_change_channel_when_off(self):
        self.assertFalse(self.tv.is_On_status())
        self.tv.channelUp()
        self.tv.channelUp()
        self.assertEqual(0,self.tv.getChannel())

    def test_that_television_does_not_increase_volume_beyond_a_limit(self):
        self.tv.turnOn()
        for i in range (200):
            self.tv.increaseVolume()
        self.assertEqual(30,self.tv.getvolumeLevel())


if __name__ == '__main__':
    unittest.main()
