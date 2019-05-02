
import numpy as np

def test_edge_cases(algo):
    # empty 
    np.testing.assert_array_equal(algo([]), [])
    # one element 
    np.testing.assert_array_equal(algo([1]), [1])
    # sorted already 
    np.testing.assert_array_equal(algo([1,2,3,4,5]), [1,2,3,4,5])
    # reverse sorted 
    np.testing.assert_array_equal(algo([5,4,3,2,1]), [1,2,3,4,5])
    # negative numbers 
    np.testing.assert_array_equal(algo([-5,5,-1,1,0]), [-5,-1,0,1,5])
    # even count of numbers 
    np.testing.assert_array_equal(algo([-5,-1,1,0]), [-5,-1,0,1])

def test_random_cases(algo, n_tests=100, size=50):
    for test in range(n_tests):
        x = np.random.randint(1e6, size=1000)
        expected = sorted(x.copy())
        actual = algo(x.copy())
        np.testing.assert_array_equal(expected, actual)

def test_sorting_algorithm(algo, n_tests=10, size=50):
    test_edge_cases(algo)
    test_random_cases(algo, n_tests=n_tests, size=size)
    print('all tests pass!')

