import math

def unstable_poisson(input, target):
    return input - target * math.log(input)

def test_poissonU():
    assert unstable_poisson(0.5, 0.0) == 0.0
    assert unstable_poisson(1.0, 0.5) == 1.0