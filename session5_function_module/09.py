"""
Variable Number of Variables

Sometimes when you make a function you may not know the 
number of arguments coming in.

Say, you want to make an addition function where the user
can send any number of values.
"""

def addition(x,y):
    """Returns sum of two numbers"""
    return x + y

print(addition(4, 5))
# Output: 9

# print(addition(4, 5, 13))
# TypeError: addition() takes 2 positional arguments 
# but 3 were given

"""
You cannot pass three or more arguments to this function.

Let us modify this function to make that happen
"""

def addition(*values):
    """Returns added some of any number of values"""
    total = 0
    for value in values:
        total = total + value
    return total

print(addition(4, 5, 13))
# Output: 22

print(addition(9, 21, 13, 19))
# Output: 62