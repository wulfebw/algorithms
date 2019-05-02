
import numpy as np

def lcs_recursive(a,b):
    cache = dict()

    def recurse(n,m):
        if n == 0 or m == 0: 
            return 0
        elif (n,m) in cache.keys():
            return cache[(n,m)]
        else:
            if a[n-1] == b[m-1]:
                val = 1 + recurse(n-1, m-1)
            else:
                val = max(recurse(n-1, m), recurse(n, m-1))
            cache[(n,m)] = val
            return val 

    return recurse(len(a),len(b))

def lcs_iterative(a,b):
    n, m = len(a), len(b)
    table = [[0 for _ in range(m+1)]  for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                val = 1 + table[i-1][j-1]
            else:
                val = max(table[i-1][j], table[i][j-1])
            table[i][j] = val
    return table[-1][-1]

def lcs_space_optimized(a,b):
    n, m = len(a), len(b)
    v = [[0 for _ in range(m+1)] for _ in range(2)]
    for i in range(n):
        ci = i % 2
        pi = (i+1) % 2
        for j in range(m):
            if a[i] == b[j]:
                v[ci][j+1] = 1 + v[pi][j]
            else:
                v[ci][j+1] = max(v[pi][j+1], v[ci][j])
    return v[-1][-1]


if __name__ == '__main__':
    inputs = [
        ('aa','aa'),
        ('ABCDGH', 'AEDFHR'),
        ('AGGTAB', 'GXTXAYB'),
        ('babababab', 'bbbb')
    ]
    expect = [
        2,
        3,
        4,
        4
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(lcs_recursive(*i))
        print(lcs_iterative(*i))
        print()