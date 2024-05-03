class Movie:
    def __init__(self,title,rating):
        self.title = title
        # below is a non-public attribute
        self._rating = rating

#Getter 
    @property
    def rating(self):
        return self._rating
        
#Setter
    @rating.setter
    def rating(self, new_rating):
        if 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print('Please enter a new rating')


        
#create an object
my_movie = Movie("The Advenger (2012)", 4.8)

#Use the getter to access attribute __rating
print(f'This movie has a rating of {my_movie.rating}, maybe its overrated.')

#Use setter 
my_movie.rating = 5.1
print(f'This movie has a current rating of {my_movie.rating}.')