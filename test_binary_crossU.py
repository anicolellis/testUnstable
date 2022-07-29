import math

def unstable_binary_cross_entropy(input, target):
    return max(target, 0) - input * target + math.log(1 + math.exp(-1 * abs(target)))