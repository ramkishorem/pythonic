"""
Dictionary looping

Printing a dictionary did not look that pretty.
It will be useful for this purpose and many others 
to be able to loop over a dictionary.

Let us see two common ways to do it.
"""

messi = {
    'name': 'Lionel Messi',
    'age': 30,
    'country': 'Argentina',
    'club': 'Barcelona',
    'position': 'Attacker',
}

### Method 1: looping over keys
for key in messi.keys():
    print('{}: {}'.format(key, messi[key]))
# Also this is same as
# for key in messi:
# ie: Looping through the dict, loops through it's keys 
# by default


### Method 1: looping over keyvalue pair

# You need the dictionary items method for this.
# This method gives you the dictionary as a list of tuples
print(messi.items())
# Output: dict_items(
# [ ('name', 'Lionel Messi'),
# ('age', 30),
# ('country', 'Argentina'),
# ('club', 'Barcelona'),
# ('position', 'Attacker') ]
# )

for key,value in messi.items():
    # First iteration key='name', value='Lionel Messi'
    print('{}: {}'.format(key.title(), value))

# Output:
# Name: Lionel Messi
# Age: 30
# Country: Argentina
# Club: Barcelona
# Position: Attacker
