import math

def unstable_logistic(input, target):
    y = input * target
    if(y > 0):
        return math.log(1 + math.exp(-1 * y))
    return (math.log(1 + math.exp(y)) - y)