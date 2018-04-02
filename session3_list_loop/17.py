"""
2 slices of pizza

You can slice a list and use parts of it
"""

players = ['Charlotte','Merlin','Fiona','Eli','Sara']
print(players[1:3]) # Output: ['Merlin', 'Fiona']
print(players[0:3]) # Output: ['Charlotte', 'Merlin', 'Fiona']
# the 0 can be ignored
print(players[:3]) # Output: ['Charlotte', 'Merlin', 'Fiona']

# skip some elements at the start
print(players[1:]) # Output: ['Merlin', 'Fiona', 'Eli', 'Sara']
# The above notation is same as [1:-1]

# Exercise: get the last two elements
print(players['???'])  # Output: ['Eli', 'Sara']
