"""
Functions: The buildup 

Remember this part of code that we used at various places

    for key,value in details.items():
        print('{:20}: {:20}'.format(key.title(),str(value)))

We used this to print info inside a dictionary in a pretty form.

It is quite a complex-looking code. Ideally, we would like to
do something like print_dict(dictionary) and get this result
in the long run.

Let us see how to do it
"""

def print_dict(dictionary):
    """Prints a dictionary in a pretty format"""
    for key,value in dictionary.items():
        print('{:20}: {:20}'.format(key.title(),str(value)))

sanchez = {
    'name': 'Alexis Sanchez',
    'age': 29,
    'country': 'Chile',
}

print_dict(sanchez)
# Output:
# Name                : Alexis Sanchez
# Age                 : 29
# Country             : Chile

favourite_language = {
    'Charlotte': 'C',
    'Merlin': 'Python',
    'Fiona': 'Ruby',
    'Eli': 'Python',
    'Sara': 'JavaScript',
}

print_dict(favourite_language)
# Output:
# Charlotte           : C
# Merlin              : Python
# Fiona               : Ruby
# Eli                 : Python
# Sara                : JavaScript