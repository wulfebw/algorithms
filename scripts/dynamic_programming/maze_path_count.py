
import numpy as np

def count_paths(a):
    n,m = a.shape
    v = np.zeros((n+1,m+1))
    for i in range(n):
        for j in range(m):
            count = 0
            # set first cell count to one 
            # not that given this implementation, you can't start with 
            # initial conditions because the values get overwritten by count = 0
            if i == 0 and j == 0:
                count += 1
            # not in first row and above not barrier
            if i != 0 and a[i-1,j] == 0: 
                count += v[i,j+1]
            # not in first col and left not barrier
            if j != 0 and a[i,j-1] == 0:
                count += v[i+1,j]
            v[i+1,j+1] = count
    print(v)
    return int(v[-1,-1])

if __name__ == '__main__':
    inputs = [
        [[0,0,0,0],
         [0,-1,0,0],
         [-1,0,0,0],
         [0,0,0,0]]
    ]
    inputs = [np.array(a) for a in inputs]
    expect = [
        4
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(count_paths(i))
        print()