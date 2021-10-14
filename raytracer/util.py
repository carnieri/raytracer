EPSILON = 0.00001

def equal(a, b, epsilon=EPSILON):
    return abs(a - b) < epsilon
