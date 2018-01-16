
import numpy as np

def min_cost_path(a):
    n, m = np.shape(a)
    # i and j will index into the previous cells in v, but cur cells in a
    v = np.zeros((n+1,m+1))
    for i in range(n):
        for j in range(m):
            if i == 0: # must come from left
                mincost = a[i,j] + v[i+1,j]
            elif j == 0: # most come from above
                mincost = a[i,j] + v[i,j+1]
            else:
                mincost = a[i,j] + min(v[i,j],v[i+1,j],v[i,j+1])
            v[i+1,j+1] = mincost
    return int(v[-1,-1])

if __name__ == '__main__':
    inputs = [
        [[1,1],
         [1,1]],

        [[1,2,4],
         [1,9,2],
         [4,5,5]],

        [[1,2,3,9],
         [5,4,3,2],
         [3,4,5,9],
         [7,8,9,5]]

    ]
    inputs = [np.array(i) for i in inputs]
    expect = [
        2,
        10,
        15
    ]
    for (i,e) in zip (inputs, expect):
        print(e)
        print(min_cost_path(i))
        print()