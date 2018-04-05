"""
Updating attributes

The example from last program was not of much use to us.
It always says zero. Let us see how we can keep that updated.
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
        # Count is updated every time play_movie is called
        self.movie_play_count += 1
        print("{} is being played".format(self.movie))
    
    # For brevity, play_ad method is truncated
    
    def view_movie_play_count(self):
        """
        shows the number of times this screen has played a movie
        """
        print("This screen has played movie {} time(s)".format(
            self.movie_play_count
        ))

screen3 = ScreenControl('Rampage', 'Documentaries')
screen3.view_movie_play_count()
# Output: This screen has played movie 0 time(s)
screen3.play_movie()
# Output: Rampage is being played
screen3.view_movie_play_count()
# Output: This screen has played movie 1 time(s)
screen3.play_movie()
# Output: Rampage is being played
screen3.view_movie_play_count()
# Output: This screen has played movie 2 time(s)
