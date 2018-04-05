"""
Encapsulating parent-relevant attributes

Using the *args and **kwargs way of receiving arbitrary arguments
We can encapsulate arguments that only the parent class methods 
use and not worry about them in the child class methods.
"""
from screen_control import ScreenControl

class Screen3DControl(ScreenControl):
    """3D screen control inherited class"""
    def __init__(self, movie, ad_reel=None,
        last_3d_maintenance=None):
        self.last_3d_maintenance = last_3d_maintenance
        super().__init__(movie, ad_reel)

"""
This part can be written without worrying about movie
and ad_reel arguments as below
"""

class Screen3DControl(ScreenControl):
    """3D screen control inherited class"""
    def __init__(self, *args, last_3d_maintenance=None, **kwargs):
        self.last_3d_maintenance = last_3d_maintenance
        print(args) # Here just to see the args value
        print(kwargs) # Here just to see the kwargs value
        # There can be 100 levels of parents with 100s of arguments
        # in total. We can just pass them up using following line
        super().__init__(*args, **kwargs)

screen7_3d = Screen3DControl(
    'Avengers',
    last_3d_maintenance='2018-01-01')
# Output:
# ('Avengers',)
# {}

screen7_3d = Screen3DControl(
    'The Incredibles 2',
    ad_reel='Documentaries',
    last_3d_maintenance='2018-01-01',)
# Output:
# ('The Incredibles 2',)
# {'ad_reel': 'Documentaries'}

"""
Another rule to pick up here. Non-arbitrary arguments have to 
come before arbitrary arguments. For example

    def __init__(self, *args, **kwargs, last_3d_maintenance=None):
                                                        ^
will throw "SyntaxError: invalid syntax"
"""