'''
This problem is very similar to the problem asking whether a set can be 
sampled with replacement to sum to a number 
the only difference is that in this case we are also interested in the cost of 
doing so

The optimal substructure is that if you know the min cost to find everything 
for n - 1, then finding the cost for n is just a matter of asking for each 
weight j whether or not to include that weight

the value matrix in this case is filled as 
each cell indicates the min cost possible to reach that cell where the row 
indicates the weight and the column indicates the minimum cost possible using 
only weights up to and including the jth column
'''
import numpy as np

def min_cost_weight(n, c):
    m = len(c)
    v = np.ones((n+1,m+1)) * np.inf
    v[0,:] = 0
    for i in range(n):
        for j in range(m):
            if (i+1) - (j+1) >= 0:
                mincost = min(v[i+1-(j+1),j+1] + c[j], v[i+1,j])
            else:
                mincost = v[i+1,j]
            v[i+1,j+1] = mincost
    return v[-1,-1]

if __name__ == '__main__':
    inputs = [
        (5, [20, 10, 4, 50, 100]),
        (5, [1, 10, 4, 50, 100]),
        (5, [1, 2, 3, 4, 5]),
        (5, [np.inf, np.inf, 4, 5, np.inf])
    ]
    expect = [
        14,
        5,
        5,
        np.inf
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(min_cost_weight(*i))
        print()