"""
Sort that out

Let us see how to sort, reverse, measure lists
"""

# permanent sorting
cars = ['Hyundai', 'Ford', 'Toyota', 'Skoda']
print(cars) # Output: ['Hyundai', 'Ford', 'Toyota', 'Skoda']
cars.sort()
print(cars) # Output: ['Ford', 'Hyundai', 'Skoda', 'Toyota']
cars.sort(reverse=True) # descending
print(cars) # Output: ['Toyota', 'Skoda', 'Hyundai', 'Ford']


# permanent sorting
cars = ['Hyundai', 'Ford', 'Toyota', 'Skoda']
print(cars) # Output: ['Hyundai', 'Ford', 'Toyota', 'Skoda']
print(sorted(cars)) # Output: ['Ford', 'Hyundai', 'Skoda', 'Toyota']
print(cars) # Output: ['Hyundai', 'Ford', 'Toyota', 'Skoda']

# reverse without sorting
cars.reverse()
print(cars) # Output: ['Skoda', 'Toyota', 'Ford', 'Hyundai']

# length of the list
print(len(cars)) # Output: 4
