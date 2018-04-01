"""
The Range Looper

You can use the range function to loop over a sequence 
of numbers.
"""

for number in range(5):
    print(number)

# Output:
# 0
# 1
# 2
# 3
# 4

"""
Note that it starts at 0, not 1 and goes until 4,not 5
"""

# different starting point
for number in range(2,6):
    print(number)

# Output:
# 2
# 3
# 4
# 5

# Creating a list from range
count_to_ten = list(range(1, 11))
print(count_to_ten) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Stepping
odd_ones = list(range(1, 11, 2))
print(odd_ones) # Output: [1, 3, 5, 7, 9]

# Stepping
even_ones = list(range(11)) # ?? fix this
print(even_ones) # Output: [0, 2, 4, 6, 8, 10]
