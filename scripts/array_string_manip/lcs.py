
import numpy as np

import context_timer as ct

def lcs(a,b):
    n, m = len(a), len(b)
    v = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                v[i+1][j+1] = 1 + v[i][j]
            else:
                v[i+1][j+1] = max(v[i+1][j], v[i][j+1])
    return v[-1][-1]

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

    n_tests = 10
    length = 50
    tests = np.random.randint(ord('A'), ord('Z') + 1, size=n_tests * length * 2)
    tests = tests.reshape(n_tests, 2, length)
    letter_tests = []
    for i in range(n_tests):
        a = ''.join([chr(v) for v in tests[i,0]])
        b = ''.join([chr(v) for v in tests[i,1]])
        letter_tests.append((a,b))

    with ct.ContextTimer():
        for (a,b) in letter_tests:
            expected = lcs(a,b)
    with ct.ContextTimer():
        for (a,b) in letter_tests:
            actual = lcs_space_optimized(a,b)
