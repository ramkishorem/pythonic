"""
Argument order matters ... or not
"""

def greet_and_update(name, day):
    """greet a person and update them number of service days"""
    print('Hello {}. It\'s your day {}.'.format(name, day))


greet_and_update(144, 'Eli')
# Output: Hello 144. It's your day Eli.

"""
What???
you have to pass arguments in the corresponding order as 
the parameters

if you want to pass arguments without worrying about order
you can pass them with the parameter name
"""

greet_and_update(day=144, name='Eli')
# Output: Hello Eli. It's your day 144.

"""
When you pass arguments along with the parameter name,
they are called 'KEYWORD arguments'
"""