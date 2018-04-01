"""
Keys and values

Let us look at a dictionary definition closely.
"""

messi = {
    'name': 'Lionel Messi',
    'age': 30,
    'country': 'Argentina',
    'club': 'Barcelona',
    'position': 'Attacker',
}

"""
this is how we define a dictionary.
values to the left of : are 'keys'
values to the right of : are, well, 'values'
Together, we call each a 'key-value pair'
"""

# we can get a list of all keys are by all values
print(messi.keys())
# Output: dict_keys(['name', 'age', 'country',
#                   'club', 'position'])

print(messi.values())
# Output: dict_values(['Lionel Messi', 30, 'Argentina',
#                    'Barcelona', 'Attacker'])
