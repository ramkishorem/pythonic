"""
Multiple parameters and arguments

A function can have multiple parametres and arguments
"""

def greet_and_update(name, day):
    """greet a person and update them number of service days"""
    print('Hello {}. It\'s your day {}.'.format(name, day))

# first argument Dora is assigned to name, first parameter
# second argument 7 is assigned to day, second parameter
greet_and_update('Dora', 7)
# Output: Hello Dora. It's your day 7.


# A function can be called as many times as you want
greet_and_update('Finn', 23)
# Output: Hello Finn. It's your day 23.
