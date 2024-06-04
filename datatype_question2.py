# Question 2
# In the tutorial, you learned about booleans (which can take a value of True or False), in addition to integers, floats, and strings. For this question, your goal is to determine what happens when you multiply a boolean by any of these data types. Specifically,

# What happens when you multiply an integer or float by True? What happens when you multiply them by False? How does the answer change if the numbers are positive or negative?
# What happens when you multiply a string by True? By False?
# Use the next code cell for your investigation.

# code:

print(3 * True)
print(-3.1 * False)
print("abc" * False) #produce empty space
print(type("abc" * False))
print(len("abc" * False))
