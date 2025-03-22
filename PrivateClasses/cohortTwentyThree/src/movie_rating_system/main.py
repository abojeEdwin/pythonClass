import sys
from cohortTwentyThree.src.movie_rating_system.movie import Movie

class Main:
    title = " "
    rating = " "
    message = """
        1 -> Add a movie
        2 -> Rate a movie
        3 -> View average rating for a movie
        4 -> View average ratings of all movies
        5 -> Exit
    """
    while True:
        choice = input(message)

        if choice == "1":
            movie  = Movie()
            title = input("Enter movie title: ")
            movie.add_movie(title)


        if choice == "2":
            movie = Movie()
            title = input("Enter movie title: ")
            rating = input("Enter your rating: ")
            movie.add_rating(title,rating)

        if choice == "3":
            movie = Movie()
            title = input("Enter movie title: ")
            movie.get_average_rating(title)

        if choice == "4":
            pass