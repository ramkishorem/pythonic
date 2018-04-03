"""
Variable Number of Variables: Part 2

let us write a function to calculate the magnitude of a vector
"""
def vector_magnitude(i, j, k):
    """Returns magnitude of the given vector"""
    square_sum = i * i + j * j + k * k
    return square_sum ** (1/2)

print(vector_magnitude(2, 3, 6))
# Output: 7.0

"""
How would you normally store a vector value in a variable?
I would suggest a tuple
"""
v1 = (4, 8, 3)

"""
Now let us use our function to calculate the magnitude of 
this vector
"""
print(vector_magnitude(v1))
# TypeError: vector_magnitude() missing 2 required 
# positional arguments: 'j' and 'k'

"""
You are not passing three arguments to the function that it 
expects. So what can we do?
"""
print(vector_magnitude(v1[0], v1[1], v1[2]))
# Output: 9.433981132056603

"""
This is a bit tedious right? what if you are dealing with  
seven dimensional vectors?

there is an easier way
"""
print(vector_magnitude(*v1))
# Output: 9.433981132056603

"""
Very similar to how we received variable number of arguments,
here we do it when we passed arguments.
The tuple splits into its components before entering the function.
Values are automatically assigned to i, j, k

i.e      i, j, k = *(4, 8, 3) = 4, 8, 3
"""