"""
Inheritance

Some of the screens in our theatre have 3D support. 
We have some special needs for these screens like tracking
the last maintenance date of the 3D system.

We don't have to write the new fresh class. We can use the 
features already available on our ScreenControl class.
"""
# Our full ScreenControl class is in this module for import
from screen_control import ScreenControl

# Let us inherit from it
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

screen6_3d = Screen3DControl(
    'Ready Player one',
    'English Trailers',
    '2018-04-01',
    )

screen6_3d.view_last_3d_maintenance()
# Output: Last 3D maintenance was performed on 2018-04-01

# Calling parent class methods
screen6_3d.play_movie()
# Output: Ready Player one is being played

screen7_3d = Screen3DControl(
    'The Incredibles 2',
    )

screen7_3d.view_last_3d_maintenance()
# Output: No record of maintenance