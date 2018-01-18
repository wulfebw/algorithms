'''
How's floyd warshall work?
It's in the same vein as the "sum up to using items" problems 
essentially, it orders are the vertices and then asks
using all the vertices up to k, what's the best way to get from u to v?
the answer is either 
1. don't use k and just use the previous best route from u to v 
2. use k, in which case the best route is from u to k + from k to v 

For m vertices, it fills in a matrix of shape (m,m,m+1)
let the last dimension indicate which vertices are being used (i.e., k)
and the other two indicate the best distances so far

Thus the first slice of this matrix is just the adjacency matrix 
and the last slice after running the algorithm is the all pairs shortest path matrix
'''

import numpy as np

from context_timer import ContextTimer

def floyd_warshall(a):
    m = len(a)
    v = np.ones((m,m,m+1)) * np.inf
    v[:,:,0] = a
    for i in range(1, m+1):
        for j in range(m):
            for k in range(m):
                v[j,k,i] = min(
                    v[j,k,i-1], # don't use this vertex
                    v[j,i-1,i-1] + v[i-1,k,i-1] # do use this vertex
                )
    return v[:,:,-1]

def floyd_warshall_fast(a):
    '''
    don't need to keep around past values
    '''
    m = len(a)
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if a[j,k] > a[j,i] + a[i,k]:
                    a[j,k] = a[j,i] + a[i,k]
    return a

if __name__ == '__main__':

    side = 200
    random_adj_mat = np.random.rand(side * side) * side
    mask = np.random.rand(side ** 2) < .8
    random_adj_mat[mask] = np.inf
    random_adj_mat = (random_adj_mat).reshape(side,side)

    inputs = [
        [[0,np.inf,1],
         [1,0,np.inf],
         [np.inf,1,0]],

        [[0,   5,  np.inf, 10],
         [np.inf,  0,  3,  np.inf],
         [np.inf, np.inf, 0,   1],
         [np.inf, np.inf, np.inf, 0]],

        random_adj_mat
    ]
    inputs = [np.array(a) for a in inputs]
    expect = [
        [[0,2,1],
         [1,0,2],
         [2,1,0]],

        [[0,5,8,9],
         [np.inf,0,3,4],
         [np.inf,np.inf,0,1],
         [np.inf,np.inf,np.inf,0]],

        'no idea'
    ]
    expect = [np.array(a) for a in expect]
    for (i,e) in zip(inputs, expect):
        print(e)
        with ContextTimer():
            print(floyd_warshall(i.copy()))
        with ContextTimer():
            print(floyd_warshall_fast(i.copy()))















