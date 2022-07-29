def unstable_sum_squares(a, b, c):
    X_vector = [a, b, c]
    n = 0
    summation = 0
    sum_square = 0
    for x in X_vector:
        n += 1
        summation += x
        sum_square += x * x
    SS = (sum_square - (summation * summation)/n)
    return SS

def test_sum_squaresU():
    assert unstable_sum_squares(100.0, 100.0, 100.0) == 0.0

    assert unstable_sum_squares(100.0, 1000.0, 10000.0) == 29970000.0