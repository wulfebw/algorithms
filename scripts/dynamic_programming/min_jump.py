
import numpy as np

def min_jump(a):
    n = len(a)
    v = np.ones(n) * np.inf
    v[0] = 0
    for i in range(n):
        for j in range(i):
            if a[j] >= i - j:
                v[i] = min(v[i], v[j] + 1)
    return int(v[-1])

if __name__ == '__main__':
    inputs = [
        [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9],
    ]
    expect = [
        3
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(min_jump(i))
        print()