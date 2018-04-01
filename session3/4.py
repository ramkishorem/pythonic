"""
Fancy word alert: Mutable

In Python, lists are mutable. What does that mean? 
Individual values in the list can be modified or new 
values can be added
"""
# Modifying
cars = ['Honda','Ford','Toyota']
print(cars) # Output: ['Honda', 'Ford', 'Toyota']
cars[0] = 'Hyundai'
print(cars) # Output: ['Hyundai', 'Ford', 'Toyota']

# Appending(add at the end)
cars.append('Skoda')
print(cars) # Output: ['Hyundai', 'Ford', 'Toyota', 'Skoda']
