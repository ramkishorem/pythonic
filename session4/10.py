"""
Dictionception: It's actually very common

You can even have a dictionary inside another dictionary.
Tthis is a common way to store data
"""

manutd = {
    'Paul Pogba': {
        'age': 24,
        'country': 'France',
    },
    'Alexis Sanchez': {
        'age': 29,
        'country': 'Chile',
    },
    'Romelu Lukaku': {
        'age': 25,
        'country': 'Belgium',
    }
}

# to get to the information
for player, details in manutd.items():
    print(player)
    for key,value in details.items():
        print('    {:10}: {:30}'.format(key.title(),str(value)))
    print()

# Output:
# Paul Pogba
#     Age       : 24
#     Country   : France

# Alexis Sanchez
#     Age       : 29
#     Country   : Chile

# Romelu Lukaku
#     Age       : 25
#     Country   : Belgium
