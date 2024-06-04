# Question 3
# In this question, you will build off your work from the previous exercise to write a function that estimates the value of a house.

# Use the next code cell to create a function get_expected_cost that takes as input three variables:

# beds - number of bedrooms (data type float)
# baths - number of bathrooms (data type float)
# has_basement - whether or not the house has a basement (data type boolean)
# It should return the expected cost of a house with those characteristics. Assume that:

# the expected cost for a house with 0 bedrooms and 0 bathrooms, and no basement is 80000,
# each bedroom adds 30000 to the expected cost,
# each bathroom adds 10000 to the expected cost, and
# a basement adds 40000 to the expected cost.
# For instance,

# a house with 1 bedroom, 1 bathroom, and no basement has an expected cost of 80000 + 30000 + 10000 = 120000. This value will be calculated with get_expected_cost(1, 1, False).
# a house with 2 bedrooms, 1 bathroom, and a basement has an expected cost of 80000 + 2*30000 + 10000 + 40000 = 190000. This value will be calculated with get_expected_cost(2, 1, True).

# code:

def get_expected_cost(beds, baths, has_basement):
    value = 80000+30000*float(beds)+10000*float(baths)+40000*bool(has_basement)
    return value
