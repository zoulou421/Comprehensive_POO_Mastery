"""
Working with heritage classes
"""
movies=["private_Preacher series","public_My Strongold", "private_Fortifier"]

class UserHeritage2:
    def __init__(self, name, first_name):
        self.name=name
        self.first_name=first_name
    def __str__(self):
        return  f"User {self.name} {self.first_name}"

    def show_movies(self):
        for movie in movies:
            print(movie)

class PublicUser(UserHeritage2):
    def __init__(self,name, first_name):
        #UserHeritage2.__init__(self,name,first_name) you replace it with super() as follows:
        super().__init__(name,first_name)
    def show_movies(self):
        for movie in movies:
            if not movie.startswith("private_"):
             print(movie)


myUser= PublicUser("BEBY", "Bonevy")
myUser.show_movies()


