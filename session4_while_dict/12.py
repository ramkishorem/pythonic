"""
A U B

A set is similar to it in mathematics.
It is an unordered collections of UNIQUE elements.
It is also represented with curly braces same as maths.
"""
python_lovers = {'Bill','Ron','Aaron','Padme'}
javascript_lovers = {'Fred','George','Ryan','Padme','Ron'}

# Union
print(python_lovers | javascript_lovers)
# Output: {'Bill', 'Padme', 'George', 'Ron', 'Aaron',
# 'Ryan', 'Fred'}

# Intersection
print(python_lovers & javascript_lovers)
# Output: {'Padme', 'Ron'}

# Difference (A and not B)
print(python_lovers - javascript_lovers)
# Output: {'Aaron', 'Bill'}

# Exists
print('Bill' in python_lovers) # Output: True
print('Ron' not in python_lovers) # Output: False

# Is subset
print({'Aaron','Ron'} <= python_lovers) # Output: True

# Is superset
print(javascript_lovers <= {'Fred','Ron'}) # Output: False
