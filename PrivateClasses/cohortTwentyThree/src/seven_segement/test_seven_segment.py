import unittest
import segments



class MyTestCase(unittest.TestCase):
    def test_that_A_displays(self,):
        hex_num = 0x30
        actual = segments.A(hex_num)
        expected = ' '
        self.assertEqual(actual, expected)

    def test_that_B_displays(self,):
        hex_num = 0x30
        actual = segments.B(hex_num)
        expected = '#'
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
