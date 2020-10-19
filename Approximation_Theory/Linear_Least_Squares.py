#Methods for finding the linear formula for least squares

def linear_least_squares(x, y):
    """
    Use the least squares method to find the line that
    best fits points of a graph

    x: array of all x values
    y: array of all y values

    returns lambda expression of the line of least squares
    """
    #Check to make sure each x has a y value...
    if len(x) != len(y):
        return 'failure'
    #get m
    m = len(x)
    #get appropriate sums
    x_sum = 0
    x_sq_sum = 0
    y_sum=0
    xy_sum = 0
    for i in zip(x,y):
        x_sum += i[0]
        x_sq_sum += i[0]**2
        y_sum += i[1]
        xy_sum += i[0] * i[1]
    a0 = (x_sq_sum * y_sum - xy_sum * x_sum)/(m * x_sq_sum - (x_sum)**2)
    a1 = (m * xy_sum - x_sum * y_sum) / (m * x_sq_sum - (x_sum)**2)

    print(str(a1) + 'x + ' + str(a0))
    return lambda x: a1 * x + a0
"""
x = [1,2,3,4,5,6,7,8,9,10]
y = [1.3,3.5,4.2,5.0,7,8.8,10.1,12.5,13,15.6]

f = linear_least_squares(x,y)
"""
