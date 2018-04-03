"""
The Function Scope

Python functions have their own 'scopes'.

Values received by the parameters and any new 
variables created inside the functions exist only inside 
the function.

Modifying a parameter value will not modify any variable 
outside the function.
"""

public_value = 5

def foo(function_value):
    function_value = function_value + 5
    print(function_value)

foo(public_value) # Output: 10
print(public_value) # Output: 5

"""
This is why, to preserve changes we have to return values.


Lists, dictionaries on the other hand work differently to 
save memory.
"""

public_list = [1, 2, 3]
public_dict = {'a': 4}

def fii(function_list, function_dict):
    function_list[2] = 5
    function_dict['a'] = 6
    print(function_list)
    print(function_dict)

fii(public_list, public_dict)
# Output: 
# [1, 2, 5]
# {'a': 6}

print(public_list)# Output: [1, 2, 5]
print(public_dict)# Output: {'a': 6}

"""
Original list and dictionary values are changed
"""