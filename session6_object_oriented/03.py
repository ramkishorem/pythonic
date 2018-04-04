"""
The __init__ method

Attributes and Methods:
    We mentioned situations and behaviours when describing 
    classes.

    Situations are modelled using 'attributes', also called 
    'member variables' in some languages.

    Behaviours are modelled using 'methods', alse called
    'member functions' in some languages.

__init__ is the method that is called implicitly when the 
class is instantiated. So, this is the method that you use to 
initialise attributes of an instance.

Let us see how to instantiate a class
"""
screen1 = ScreenControl('Ready Player One', 'English Trailers')

"""
When this line is executed, __init__ method of ScreenControl 
will be called, the arguments within the brackets will be 
passed to it.

    __init__(self, movie, ad_reel):

the first parameter of a normal Python method is always the 
instance itself (hence, we call it 'self'). It is passed 
implicitly. You don't have to pass it. Just have it as the 
first parameter.

We have two other parameters 'movie' and 'ad_reel'. 
'Ready Player One' is assigned to movie and 'English Trailers' 
to ad_reel. This behaviour is similar to function call.

Inside the method, we initialise the attributes from the 
parameter values.
    # instance attribute     parameter
    self.movie          =    movie
    self.ad_reel        =    ad_reel

Unlike variables defined inside a function, instance attributes
are preserved between method calls. So, you can use these 
attributes in other methods.

There are more 'magic methods' with __method__ name structure called
 that python calls implicitly. We'll just use __init__ for now.
"""