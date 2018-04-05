"""
Overriding the parents

You can override the methods on the parent to have a modified
behaviour on the child.
"""
from screen_control import ScreenControl

class Screen3DControl(ScreenControl):
    def __init__(self, *args, last_3d_maintenance=None, **kwargs):
        self.last_3d_maintenance = last_3d_maintenance
        super().__init__(*args, **kwargs)

    def play_movie(self):
        print("3D movie {} is being played".format(self.movie))

screen1_3d = Screen3DControl('Avengers', 'English trailers')
screen1_3d.play_movie() # calls play_movie on Screen3DControl
# Output: 3D movie Avengers is being played

# Instantiating parent class
screen2 = ScreenControl('Rampage', 'Documentaries')
screen2.play_movie() # calls play_movie on ScreenControl
# Output: Rampage is being played

# Method that was not overridden
screen1_3d.play_ad() # still calls play_ad on ScreenControl
# Output: Ad English trailers is being played

# Just one more issue to address
screen1_3d.view_movie_play_count()
# Output: This screen has played movie 0 time(s)

"""
But we have already played the movie once. Since we are overriding
parent play_movie method and not calling the parent method using
super(), the
    self.movie_play_count += 1
on the parent method is not running anymore. We have to add that
to the child method too.
"""
class Screen3DControl(ScreenControl):
    def __init__(self, *args, last_3d_maintenance=None, **kwargs):
        self.last_3d_maintenance = last_3d_maintenance
        super().__init__(*args, **kwargs)

    def play_movie(self):
        self.movie_play_count += 1 # Add incrementing logic
        print("3D movie {} is being played".format(self.movie))
