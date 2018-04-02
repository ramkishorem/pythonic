"""
Know the language enough to write my own dictionary.

So far, we saw to 'iterable(loopable)' data structures,
lists and tuples. They have one key thing in common.
They have integer indices. eg: [2], [-1], [1:7]...

Let us see the limitation of that in some use cases.
"""

# Say, we want to store info about players in lists

messi = ['Lionel Messi', 30, 'Argentina', 'Barcelona', 'Attacker']
ramos = ['Sergio Ramos', 33, 'Spain', 'Real Madrid', 'Defender']

# get Messi's country
print(messi[2])

# get Ramos's club
print(ramos[3])

"""
This is not very desirable. We have to remember which index 
corresponds to which information. It is prone to errors 
when we add new players.

Would you rather it be
    print(messi['country'])
    print(ramos['club'])
? isn't this more readable and make more sense?

we can use dictionaries to do that.
"""

messi = {
    'name': 'Lionel Messi',
    'age': 30,
    'country': 'Argentina',
    'club': 'Barcelona',
    'position': 'Attacker',
}

ramos = {
    'name': 'Sergio Ramos',
    'age': 33,
    'country': 'Spain',
    'club': 'Real Madrid',
    'position': 'Defender',
}

print(messi['country']) # Output: Argentina
print(ramos['club']) # Output: Real Madrid
