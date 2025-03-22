from datetime import datetime

class Movie:
    def __init__(self):
        self.counter = 1
        self.movie_dict = {}
        self.movie_list =[]
        self.ratings = []
        self.app_ratings = []


    user_date_time = datetime.now()

    def get_movie(self,title):
        for movie in self.movie_dict.items():
            if movie[1] == title:
                return movie
        return "Movie not found"

    def get_movie_rating(self,title):
            for items in self.ratings:
                if items[0] == title:
                    return items[1]
            return "Movie not found"

    def add_movie(self,title):
        try:
            if title not in self.movie_dict.values():
                self.movie_dict[self.counter] = title
                self.counter += 1
                self.movie_list.append(self.movie_dict)
                print(f'{title} added successfully')
            else:
                raise ValueError("Movie already exist in the system")
        except:
                print("Something went wrong")
                raise ValueError

    def get_movie_list_size(self):
        return len(self.movie_list)

    def add_rating(self,title,rating):
        movie_name = self.get_movie(title)
        if isinstance(movie_name, str):
            raise ValueError (movie_name)
        if type(rating) is not int or rating < 1 or rating > 5:
            return "Rating must be between 1 and 5"

        self.ratings.append([title, rating])
        return f"{title} rating added"

    def get_average_rating(self, title):
        total = 0
        counter = 0
        average = 0
        try:
            if title not in self.movie_dict.values():
                print("Movie not found")
            else:
                for items in self.ratings:
                    if items[0] == title:
                        total +=items[1]
                        counter += 1

                    average = total / counter
                return average
        except ValueError:
            print("Movie not found")

    def get_all_average_ratings(self):
        average = 0
        total = 0
        counter = 0
        for ratings in  self.ratings:
            total+= ratings[1]
            counter+=1
            if counter == 0:
                raise ValueError("Cannot divide by zero")
        average = total / counter
        return average



