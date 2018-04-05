"""
Default value for attributes

The theatre client calls you and asks for a way to track and 
view the number of times the screen has played a movie.

This count always starts at 0 when a new screen is instantiated.
"""

class ScreenControl:
    """Simple cinema screen control"""

    def __init__(self, movie, ad_reel):
        """movie and ad_reel are initialised"""
        self.movie = movie
        self.ad_reel = ad_reel
        self.movie_play_count = 0
    
    def play_movie(self):
        """control to play the movie"""
        print("{} is being played".format(self.movie))
    
    def play_ad(self):
        """control to play the ad reel"""
        print("Ad {} is being played".format(self.ad_reel))
    
    def view_movie_play_count(self):
        """
        shows the number of times this screen has played a movie
        """
        print("This screen has played movie {} time(s)".format(
            self.movie_play_count
        ))

screen3 = ScreenControl('Rampage', 'Documentaries')
screen3.view_movie_play_count()
# Output:
# This screen has played movie 0 time(s)