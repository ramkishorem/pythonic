"""
The Other Methods

We defined 2 other methods. since these don't need any other 
information, they have only the self parameter.

Let us see, how we can use them.
"""

# Get the class definition from 02

# initialise the instance
screen1 = ScreenControl('Ready Player One', 'English Trailers')

# call methods
screen1.play_movie()
# Output: Ready Player One is being played
screen1.play_ad()
# Output: Ad English Trailers is being played

"""
You call methods similar to functions but with the dot notation
similar to how you used functions in imported modules. These 
methods can use existing attributes.

They can also edit attributes or add new ones. 
"""