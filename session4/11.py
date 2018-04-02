"""
The Unique Set
"""
favourite_language = {
    'Charlotte': 'C',
    'Merlin': 'Python',
    'Fiona': 'Ruby',
    'Eli': 'Python',
    'Sara': 'JavaScript',
}

"""
Now the requirement is to see what are the languages 
people because their favourites.

we can do that by doing favourite_language.values()
"""
print(favourite_language.values())
# Output:
# dict_values(['C', 'Python', 'Ruby', 'Python', 'JavaScript'])

"""
The problem here is that I see Python twice.
That is usually not desirable.

Can you fix this problem? Using the .values() result
create a list with each language appearing only once.
"""




# You can use another datatype called 'set' to achieve this.
print(set(favourite_language.values()))
