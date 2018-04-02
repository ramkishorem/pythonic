"""
Functions: Deeper look

Functions are named blocks of code that are designed to 
do one specific job.

When you want to perform a particular task that you’ve 
defined in a function, you call the name of the function 
responsible for it.
"""

# function definition syntax
def greet_guest():
    """Prints a simple greeting"""
    print('Welcome')

# function calling/using
greet_guest() # Output: Welcome



# Passing Information to a Function
# (parameters and arguments)

# name is a 'parameter' of this function
def dynamic_greet(name):
    """greets a person with their name"""
    print('Hello {}'.format(name))

# Pass 'Merlin' to function as 'argument' when 
# calling it. It is assigned to name parameter
# upon Python entering the function.
dynamic_greet('Merlin') # Output: Hello Merlin
