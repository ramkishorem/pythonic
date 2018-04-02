"""
Insert and Delete

You may insert and delete elements at any position.
"""

# Insert
cars = ['Hyundai', 'Ford', 'Toyota', 'Skoda']
cars.insert(0,'Mercedes')
print(cars)
# Output: ['Mercedes', 'Hyundai', 'Ford', 'Toyota', 'Skoda']
cars.insert(2,'BMW')
print(cars)
# Output: ['Mercedes', 'Hyundai', 'BMW', 'Ford', 'Toyota', 'Skoda']

# Delete
del cars[2]
print(cars)
# Output: ['Mercedes', 'Hyundai', 'Ford', 'Toyota', 'Skoda']

# Pop
pull_out = cars.pop()
print(pull_out, cars)
# Output: Skoda ['Mercedes', 'Hyundai', 'Ford', 'Toyota']
pull_that_out = cars.pop(2)
print(pull_that_out, cars)
# Output: Ford ['Mercedes', 'Hyundai', 'Toyota']

# Remove by Value
cars.remove('Toyota') # Note: deletes only first occurrence
print(cars) # Output: ['Mercedes', 'Hyundai']
