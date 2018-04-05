class ScreenControl:
    """Simple cinema screen control"""

    def __init__(self, movie, ad_reel=None):
        """movie and ad_reel are initialised"""
        self.movie = movie
        self.ad_reel = ad_reel
        self.movie_play_count = 0
    
    def play_movie(self):
        """control to play the movie"""
        # Count is updated every time play_movie is called
        self.movie_play_count += 1
        print("{} is being played".format(self.movie))
    
    def play_ad(self):
        """control to play the ad reel"""
        if self.ad_reel:
            print("Ad {} is being played".format(self.ad_reel))
        else:
            print("This screen currently has no ad reel")
    
    def view_movie_play_count(self):
        """
        shows the number of times this screen has played a movie
        """
        print("This screen has played movie {} time(s)".format(
            self.movie_play_count
        ))


class Screen3DControl(ScreenControl):
    """3D screen control inherited class"""
    def __init__(self, movie, ad_reel=None,
        last_3d_maintenance=None):
        # initialising maintenance data attribute
        self.last_3d_maintenance = last_3d_maintenance
        # calling the patent(super) class's init method
        # for the rest of the initialisation work
        super().__init__(movie, ad_reel)
    
    def view_last_3d_maintenance(self):
        if self.last_3d_maintenance:
            print("Last 3D maintenance was performed on {}".\
                format(self.last_3d_maintenance))
        else:
            print("No record of maintenance")