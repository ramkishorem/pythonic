"""
List of dictionaries

you can store a roster of players with their info
in a list
"""
pogba = {
    'name': 'Paul Pogba',
    'age': 24,
    'country': 'France',
}

sanchez = {
    'name': 'Alexis Sanchez',
    'age': 29,
    'country': 'Chile',
}

lukaku = {
    'name': 'Romelu Lukaku',
    'age': 25,
    'country': 'Belgium',
}

manutd = [pogba, sanchez, lukaku]

# to get to the information
for player in manutd:
    for key,value in player.items():
        # some format techniques to print pretty
        print('{:10}: {:30}'.format(key.title(),str(value)))
    print() # to break a line

# Output:
# Name      : Paul Pogba
# Age       : 24
# Country   : France

# Name      : Alexis Sanchez
# Age       : 29
# Country   : Chile

# Name      : Romelu Lukaku
# Age       : 25
# Country   : Belgium
