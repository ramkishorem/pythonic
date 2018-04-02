"""
Do I really have to pass a value? I'm lazy

Consider this. most of the people that come to provide service
our newcomers. So their 'day' will be '1'.

Maybe we can make the function work with day parameter being 
optional. When no value is given, they should be 1 by default
"""

# parameter day has a default value
def greet_and_update(name, day=1):
    """greet a person and update them number of service days"""
    print('Hello {}. It\'s your day {}.'.format(name, day))

greet_and_update('Novisi')
# Output: Hello Novisi. It's your day 1.

# you can still provide a value for day
greet_and_update('Provisi', 320)
# Output: Hello Provisi. It's your day 320.

# We might not know the name of the person
# or not know how it is spelled or pronounced

def greet_and_update(name='friend', day=1):
    """greet a person and update them number of service days"""
    print('Hello {}. It\'s your day {}.'.format(name, day))

# new comer. Name not known
greet_and_update()
# Output: Hello friend. It's your day 1.

# familiar person but with a complex name
greet_and_update(day=14)
# Output: Hello friend. It's your day 14.
