'''
idea is that at length n on the board, you can either place 
2 horizontally or 1 vertically
both of these reduce to subproblems
with disjoint solutions (because the last tiles are different)
this just yields t(n) = t(n-1) + t(n-2)
i.e., fib seq
'''
import numpy as np

def tiling(n):
    if n <= 2: 
        return n
    v = np.zeros(n)
    v[0] = 1
    v[1] = 2
    for i in range(2, n):
        v[i] = v[i-1] +  v[i-2]
    return v[-1]

if __name__ == '__main__':
    for i in range(1, 20):
        print(i, tiling(i))