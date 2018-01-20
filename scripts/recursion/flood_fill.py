
import numpy as np

def valid_neighbors(a,x,y):
    n, m = a.shape
    neigh = []
    if x > 0:
        neigh.append((x-1,y))
    if x < n - 1:
        neigh.append((x+1,y))
    if y > 0:
        neigh.append((x,y-1))
    if y < m - 1:
        neigh.append((x,y+1))
    return neigh

def flood_fill(a,x,y,k):
    '''
    runtime:
    in the worst case visits every node, so must be at least O(nm)
    
    '''
    orig = a[x,y]
    if orig == k:
        return
    a[x,y] = k
    for (nx,ny) in valid_neighbors(a,x,y):
        if a[nx,ny] == orig:
            flood_fill(a, nx, ny, k)
    return a

if __name__ == '__main__':
    inputs = [
        (np.array([[1,2,3,4],
         [1,2,3,4],
         [1,2,3,4],
         [1,2,2,2]]),0,1,5),

        (np.array([[1,1,1,1],
         [1,2,2,1],
         [1,2,2,1],
         [1,1,1,1]]),1,1,3),

        (np.array([[1,1,1,1,1],
         [1,1,2,2,1],
         [1,1,2,1,2],
         [1,1,2,2,2]]),3,3,3),
    ]
    expect = [
        [[1,5,3,4],
         [1,5,3,4],
         [1,5,3,4],
         [1,5,5,5]],

        [[1,1,1,1],
         [1,3,3,1],
         [1,3,3,1],
         [1,1,1,1]],

        [[1,1,1,1,1],
         [1,1,3,3,1],
         [1,1,3,1,3],
         [1,1,3,3,3]]
    ]
    expect = [np.array(v) for v in expect]

    for (i,e) in zip(inputs, expect):
        print(e)
        print(flood_fill(*i))
        print()