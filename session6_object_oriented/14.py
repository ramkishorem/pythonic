"""
Variable number of variables: Part three

We have seen about passing and receiving multiple arguments
together as a tuple using *. However, this works only for 
positional(non-keyword) arguments.

But, you can also receive arbitrary keyword arguments separately
using **
"""

# it is standard to use 'args' for positional and
# 'kwargs' for keyword arguments
def arbitrary(*args, **kwargs):
    print(args)
    print(kwargs)

arbitrary('Mike', 175, 70, appearances=50, avg_rating=6.8)
# Output:
# ('Mike', 175, 70)
# {'appearances': 50, 'avg_rating': 6.8}

"""
args is a tuple and kwargs is a dictionary


There is one rule have to follow or you will see SyntaxError.
You cannot mix positional and keyword arguments in order.
All the positional arguments have to come first, followed by all 
the keyword arguments
"""
arbitrary('Mike', 175, appearances=50, 70, avg_rating=6.8)
# Error:
#     arbitrary('Mike', 175, appearances=50, 70, avg_rating=6.8)
#                                           ^
# SyntaxError: positional argument follows keyword argument
