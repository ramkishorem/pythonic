"""
Tuples

Tuple is another data type similar to list.
As you know by now, lists are mutable.
An immutable list is a tuple. You use () to define tuples 
instead of []. You still use [] to index and get a value.
"""

pillar_coordinates = (5, 3.4, 7.1)
print(type(pillar_coordinates), pillar_coordinates)
# Output: <class 'tuple'> (5, 3.4, 7.1)

# Indexing, Slicing
print(pillar_coordinates[1:])
# Output: (3.4, 7.1)

# immutable
pillar_coordinates[1] = 2.9
# TypeError: 'tuple' object does not support item assignment
pillar_coordinates.append(9.8)
# AttributeError: 'tuple' object has no attribute 'append'

# You can overwrite tuple variable like any other
pillar_coordinates = (1, 2, 3)
# pillar_coordinates now contains a completely new tuple

"""
When compared with lists, tuples are simple data structures.
Use them when you want to store a set of values that should 
not be changed throughout the life of a program.
"""