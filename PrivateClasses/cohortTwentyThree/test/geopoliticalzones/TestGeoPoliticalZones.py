import unittest
from cohortTwentyThree.src.geopoliticalzones.PoliticalZones import PoliticalZones

class MyTestCase(unittest.TestCase):
    def test_that_enum_class_returns_correct_values(self):
        self.assertEqual(('Benue', 'FCT', 'Kwara', 'Nasarawa', 'Plateau', 'Niger'),PoliticalZones.NORTH_CENTRAL.value)

if __name__ == '__main__':
    unittest.main()
