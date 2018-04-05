"""
Optional attribute

We may not always have an Ad reel. Let's just make that attribute 
optional.
"""

class ScreenControl:
    """Simple cinema screen control"""

    def __init__(self, movie, ad_reel=None):
        """movie and ad_reel are initialised"""
        self.movie = movie
        self.ad_reel = ad_reel
    
    def play_movie(self):
        """control to play the movie"""
        print("{} is being played".format(self.movie))
    
    def play_ad(self):
        """control to play the ad reel"""
        if self.ad_reel:
            print("Ad {} is being played".format(self.ad_reel))
        else:
            print("This screen currently has no ad reel")

screen4 = ScreenControl('Black Panther', 'English trailers')
screen4.play_ad()
# Output: Ad English trailers is being played
screen5 = ScreenControl('Ant Man')
screen5.play_ad()
# Output: This screen currently has no ad reel