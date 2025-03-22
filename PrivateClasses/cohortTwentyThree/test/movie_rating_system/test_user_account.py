import unittest
from cohortTwentyThree.src.movie_rating_system.user_account import UserAccount

class MyTestCase(unittest.TestCase):
    
    def test_that_user_can_add_movie(self):
        user = UserAccount()
        user.add_movie("Tenet")
        self.assertEqual({"1:Tenet"}, user.get_movie_name())  # add assertion here

if __name__ == '__main__':
    unittest.main()
