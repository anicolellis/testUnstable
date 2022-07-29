def unstable_variance(a, b, c):
    X_vector = [a, b, c]
    n = 0
    summation = 0
    sum_square = 0
    for x in X_vector:
        n += 1
        summation += x
        sum_square += x * x
    variance = (sum_square - (summation * summation)/n)/(n-1)
    return variance

def test_varianceU():
    assert unstable_variance(100.0, 100.0, 100.0) == 0.0

    assert unstable_variance(100.0, 1000.0, 10000.0) == 29970000.0

    #assert stable_variance([1e-3, 1e-12, 1e-6]) == 3.330003329996666604003873086992104646242296439595520496368408203125e-07
    #assert unstable_variance([1e-3, 1e-12, 1e-6]) == 3.330003329996666604003873086992104646242296439595520496368408203125e-07