# Question 2
# In the exercise for the previous lesson, you wrote a function cost_of_project() that estimated the price of rings for an online shop that sells rings with custom engravings. This function did not use conditional statements. In this exercise, you will rewrite the function to use conditional statements. Recall that the online shop has the following price structure:

# Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
# Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
# Spaces and punctuation are counted as engraved units.
# Your function cost_of_project() takes two arguments:

# engraving - a Python string with the text of the engraving
# solid_gold - a Boolean that indicates whether the ring is solid gold
# It should return the cost of the project.

# The function has been partially completed for you, and you need to fill in the blanks to complete the function.

# code:

def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100+10*len(engraving)
    else:
        cost = 50+7*len(engraving)
    return cost
​
