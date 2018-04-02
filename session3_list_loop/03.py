"""
The variable treatment

You may treat an indexed value like any other variable
"""
names = ['Rick','Mike','Eric']
print('{} mentioned that {} yelled, "{}"'.format(
    names[0].title(),
    names[2].title(),
    names[1].upper(),
))

# Output:
# Rick mentioned that Eric yelled, "MIKE"

"""
I am treating indexed values as strings here and am using string methods on them.
"""