"""
Modules

We have been using a built-in Python function called print.

Now this function is not part of our program. But we are still 
able to use it. Python 'imports' these built-in functions by 
default to all programs.

We can also define functions in a different module(program)
and reuse them in any of our program. let us add our average 
function to utilities module

utilities.py

def average(*values):
    return sum(values) / len(values)

We have to import our custom modules manually

"""
import utilities

values = [4, 5, 6, 7]

print(utilities.average(values)) # Output 5.5

"""
You may also choose to specifically import the average function
"""

from utilities import average
print(average(values)) # Output 5.5

"""
With this syntax, you don't need to use the dot notation 
when you call the function. Because we've explicitly 
imported average() in the import statement, we can call it 
by name when we use the function.

You can also import them as 'variable' to avoid collisions
or create short forms.
"""

from utilities import average as avg
print(avg(values)) # Output 5.5

"""
You may also import all the functions in a module using *
and used them without the module name and dot notation.

However, it's best not to use this approach when you're working
with larger modules that you didn’t write. If the module has 
a function name that matches an existing name in your program, 
you can get some unexpected results.
"""
from utilities import *