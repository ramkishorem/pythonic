"""
The Return of function

Printing values is not the only outcome of functions.
You can have a function to return a value and store it 
in a variable.
"""

def average(values):
    """Returns average of the given numeric list"""
    total = sum(values)
    count = len(values)
    return total / count

print(average([12, 7, 8, 13]))
# Output: 10.0

mean = average([55.7, 23.1, 90.7, 74.3])
print(mean)
# Output: 60.95
