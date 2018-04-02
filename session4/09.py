"""
Lists inside dictionaries

A dictionary value can be anything! even a list!
"""
pogba = {
    'name': 'Paul Pogba',
    'last 5 rating':[6.5,7.2,8.7,6.3,7.4],
}

sanchez = {
    'name': 'Alexis Sanchez',
    'last 5 rating':[7.5,6.2,7.8,6.7,7.1],
}

manutd = [pogba, sanchez]

# to get to the information
print('Average ratings:')
for player in manutd:
    name = player['name']
    ratings = player['last 5 rating']
    average = sum(ratings) / len(ratings)
    print('{:18}: {:.2f}'.format(name, average))

# Output:
# Average ratings:
# Paul Pogba        : 7.22
# Alexis Sanchez    : 7.06