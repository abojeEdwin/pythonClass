from cohortTwentyThree.src.movie_rating_system.movie import Movie


class UserAccount(Movie):
    def __init__(self):
        super().__init__()

    movie_dict = {}

    def add_movie(self, title):
        movie_dict[self.mo]