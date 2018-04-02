"""
Dictionaries: mutable or not

Like lists, dictionaries are mutable
"""

messi = {
    'name': 'Lionel Messi',
    'age': 30,
    'country': 'Argentina',
    'club': 'Barcelona',
    'position': 'Attacker',
}

# modify
messi['age'] = 31

# add new key-value
messi['height'] = 170

print(messi)
# Output:
# {'name': 'Lionel Messi', 'age': 31, 'country': 'Argentina',
# 'club': 'Barcelona', 'position': 'Attacker', 'height': 170}

# we can even define an empty dictionary and add values later
lukaku = {}
lukaku['name'] = 'Romelu Lukaku'
lukaku['position'] = 'Attacker'

# or remove with del
del messi['height']
print(messi)
# Output:
# {'name': 'Lionel Messi', 'age': 31, 'country': 'Argentina',
# 'club': 'Barcelona', 'position': 'Attacker'}
