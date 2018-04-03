"""
Drill 1: Price Check

Given a dictionary of data
"""

catalogue = {
    'PlayStation': {
        'Pro black': 40000,
        'Pro white': 42000,
        'Black': 30000,
        'Controller': 3300,
    },
    'iPhone': {
        'X White': 80000,
        '6S Grey': 33000,
        'Se Gold': 20000,
    },
    'Nike shoes': {
        'Running': 9896,
        'Downshifter': 2996,
        'Air Vapormax': 41000,
    },
}

"""
Define one check_price function here to get following outputs
for corresponding calls.
"""

check_price('PlayStation', product='black')
# Output: 30000

check_price('Nike shoes')
# Output:
# Running      : 9896
# Downshifter  : 2996
# Air Vapormax : 41000

check_price()
# Output:
# Choose a product from
# PlayStation
# iPhone
# Nike shoes

check_price('Se Gold')
# Output:
# No product found

check_price('iPhone', 2)
# Output:
# X White        : 160000
# 6S Grey        : 66000
# Se Gold        : 40000
