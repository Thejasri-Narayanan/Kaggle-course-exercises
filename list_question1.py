# Question 1
# You own a restaurant with five food dishes, organized in the Python list menu below. One day, you decide to:

# remove bean soup ('bean soup') from the menu, and
# add roasted beet salad ('roasted beet salad') to the menu.
# Implement this change to the list below. While completing this task,

# do not change the line that creates the menu list.
# your answer should use .remove() and .append().

# code:

menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp',
       'fish soup with cream and onion', 'gyro']

# TODO: remove 'bean soup', and add 'roasted beet salad' to the end of the menu
menu.remove("bean soup")
menu.append("roasted beet salad")
