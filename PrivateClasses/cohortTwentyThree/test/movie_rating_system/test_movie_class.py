import unittest
from cohortTwentyThree.src.movie_rating_system.movie import Movie

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.movie = Movie()

    def test_to_add_a_movie(self):
        movie = Movie()
        movie.add_movie("Blood diamond")
        movie.add_movie("White chicks")
        self.assertEqual(2, movie.get_movie_list_size())


    def test_that_a_movie_can_be_rated(self):
        movie = Movie()
        movie.add_movie("Tenet")
        movie.add_movie("Romeo must die")
        movie.add_rating("Romeo must die", 5)
        self.assertEqual(5,movie.get_movie_rating("Romeo must die"))

    def test_to_get_average_rating_for_a_movie(self):
        movie = Movie()
        movie.add_movie("Tenet")
        movie.add_rating("Tenet",5)
        movie.add_rating("Tenet", 2)
        movie.add_rating("Tenet", 5)
        movie.add_rating("Tenet", 3)
        self.assertEqual(3.75,movie.get_average_rating("Tenet"))

    def test_that_rating_above_5_is_not_accepted(self):
        movie = Movie()
        movie.add_movie("Naked Singlarity")
        self.assertEqual("Rating must be between 1 and 5",movie.add_rating("Naked Singlarity",10))

    def test_that_movie_is_not_added_if_movie_already_exists(self):
        movie = Movie()
        movie.add_movie("Rambo")
        self.assertRaises(ValueError,movie.add_movie,"Rambo")

    def test_to_get_all_average_ratings_of_all_movies(self):
        movie = Movie()
        movie.add_movie("Titanic")
        movie.add_movie("Iron man")
        movie.add_movie("Terminator")
        movie.add_movie("Cornan the barbarian")
        movie.add_rating("Titanic",5)
        movie.add_rating("Iron man",4)
        movie.add_rating("Terminator",4.5)
        movie.add_rating("Cornan the barbarian",3)
        self.assertEqual(4.0,movie.get_all_average_ratings())

    def test_to_raise_exception_when_trying_to_rate_a_movie_that_is_not_in_the_system(self):
        movie = Movie()
        self.assertRaises(ValueError,movie.add_rating,"In pursuit of happyness",10)




if __name__ == '__main__':
    unittest.main()
