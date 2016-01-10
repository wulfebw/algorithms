"""
:keywords: matrix multiplication, divide and conquer, Strassen
"""

import timeit
import numpy as np

def multiply_list_matricies_naive(A, B):
    """
    :description: naive multiplication of matricies

    :time: O(n^3)
    :space: O(n)

    :execution: 100000 runs on 2x2 matricies in 2.06 seconds
                1 runs on 100x100 matrix in 17.7 seconds * 1000 = 17700 second = 5 hours
    """
    size = len(A)
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            total = 0
            for k in range(size):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result

def multiply_list_matricies_numpy(A, B):
    """
    :execution: 100000 runs on 2x2 matricies in 10.34 seconds
                1000 runs on 100x100 matricies in 1.06 seconds
    """
    return np.dot(A, B)

def multiply_numpy_matricies_recursive_naive(A, B):
    """
    :description: naive recursive implementation of multiply matricies, input size must be power of 2

    :time: O(n^3)
    :space: O(1)

    :execution: 100000 runs on 2x2 matricies in 16.32 seconds
                1 runs on 100x100 matrix in 8.8 seconds * 1000 = 8800 second = 2.4 hours

    :recurrence: 8T(n/2) + Theta(n^2), first part because n (side length) is cut in half and we therefore multiply two n/2 matricies 8 times, second part because we are adding two n^2 matricies a lot of times but we disregard that in the Theta
    """
    C = np.zeros_like(A)
    def recurse(ars, are, acs, ace, brs, bre, bcs, bce):
        n = are - ars
        if n == 1:
            C[ars][bcs] += A[ars][acs] * B[brs][bcs]
        else:
            h = n/2
            i11 = 0, h, 0, h
            i12 = 0, h, h, n
            i21 = h, n, 0, h
            i22 = h, n, h, n
            # first index is A, second is B, so i11 + i11 passes in the indicies A11, B11
            recurse(*(i11 + i11))
            recurse(*(i12 + i21))     
            recurse(*(i11 + i12))                 
            recurse(*(i12 + i22))                  
            recurse(*(i21 + i11))                  
            recurse(*(i22 + i21))                  
            recurse(*(i21 + i12))                           
            recurse(*(i22 + i22))  
    s = len(A)         
    recurse(0, s, 0, s, 0, s, 0, s)      
    return C


def multiply_matricies_strassens(arr):
    raise NotImplementedError("don't think there's much value in this")

def run():
    A = [[1,2],[3,4]]
    B = [[1,0],[0,1]]
    # A = np.arange(64 * 64).reshape(64, 64)
    # B = np.eye(64)
    product = multiply_list_matricies_naive(A, B)

if __name__ == '__main__':
    t = timeit.Timer(run)
    print(t.timeit(number=100000))
    