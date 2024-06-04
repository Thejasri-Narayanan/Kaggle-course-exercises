# Question 5
# Now say you can no longer buy fractions of a gallon. (For instance, if you need 4.3 gallons to do a project, then you have to buy 5 gallons of paint.)

# With this new scenario, you will create a new function get_actual_cost that uses the same inputs and calculates the cost of your project.

# One function that you'll need to use to do this is math.ceil(). We demonstrate usage of this function in the code cell below. It takes as a number as input and rounds the number up to the nearest integer.

# code:

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_gallon=math.ceil((sqft_walls+sqft_ceiling)/(sqft_per_gallon))
    cost =(total_gallon)*cost_per_gallon
    return cost
