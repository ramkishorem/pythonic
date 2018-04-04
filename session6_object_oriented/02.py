"""
A Simple Class

Let us model a class for a cinema screen operation
"""

class ScreenControl:
    """Simple cinema screen control"""

    def __init__(self, movie, ad_reel):
        """movie and ad_reel are initialised"""
        self.movie = movie
        self.ad_reel = ad_reel
    
    def play_movie(self):
        """control to play the movie"""
        print("{} is being played".format(self.movie))
    
    def play_ad(self):
        """control to play the ad reel"""
        print("Ad {} is being played".format(self.ad_reel))

"""
There's a lot to notice here, but don't worry. You'll see this 
structure throughout this session and have lots of time to get 
used to it.
"""