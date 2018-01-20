
import numpy as np

def flip_x_o(a):
    '''
    time complexity:
    it iterates the entire grid so n * m 
    for each, it calls recurse, in the worst case, everything is an o
    in which case the internal nodes call their neighbors 
    but this can happen at most 1 time, so I'd say at worst this is 
    O((n*m)^2)


    '''
    # cache holds whether (x,y) position has o to an edge
    cache = dict()
    seen = set()
    n,m = a.shape

    def recurse(x,y):
        if a[x,y] == 'x':
            return False
        elif (x,y) in cache.keys():
            return cache[(x,y)]
        else:
            seen.add((x,y))

            if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                cache[(x,y)] = True
                return True
            else:
                cache[(x,y)] = recurse(x-1,y) or recurse(x,y-1) or recurse(x,y+1) or recurse(x+1,y)
                return cache[(x,y)]

    for i in range(n):
        for j in range(m):
            if a[i,j] == 'o' and not recurse(i,j):
                a[i,j] = 'x'

    return a

def flip_x_o_iterative(a):
    '''
    dynamic programming solution 
    basically, we need two sweeps to determine if any node can contact an edge
    so this is O(nm)

    actually this doesn't work
    '''
    print(a)
    n, m = a.shape

    # if flat then nothing will change
    if n <= 1 or m <= 1: 
        return a
    v = np.zeros((n,m), dtype=bool)
    v[np.where(a == 'o')] = True
    v[1:n-1,1:m-1] = False

    for i in range(1, n-1):
        for j in range(1, m-1):
            if a[i,j] == 'o':
                v[i,j] = v[i,j] or v[i-1,j] or v[i,j-1] or v[i+1,j] or v[i,j+1]

    for i in range(n-2, 0, -1):
        for j in range(m-2, 0, -1):
            if a[i,j] == 'o':
                v[i,j] = v[i,j] or v[i+1,j] or v[i,j+1] or v[i-1,j] or v[i,j-1]

            if not v[i,j]:
                a[i,j] = 'x'

    return a


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

    orig = a[x,y]
    if orig == k:
        return
    a[x,y] = k
    for (nx,ny) in valid_neighbors(a,x,y):
        if a[nx,ny] == orig:
            flood_fill(a, nx, ny, k)
    return a

def flip_x_o_recursive(a):
    '''
    runtime:
    O(nm + O(flood_fill)*(# of os))
    '''
    n,m = a.shape
    if n <= 1 or m <= 1:
        return a
    # replace 'o' with '-'
    a[np.where(a == 'o')] = '-'

    # find edge squares to flood fill
    b = a.copy()
    b[1:n-1,1:m-1] = 'x'
    flood_idxs = np.where(b == '-')

    for (x,y) in zip(flood_idxs[0], flood_idxs[1]):
        flood_fill(a, x, y, 'o')

    # ones that can't be reached set to x
    a[np.where(a == '-')] = 'x'

    return a


if __name__ == '__main__':
    inputs = [
        [['x','o','x','x'],
         ['x','o','x','x'],
         ['x','x','o','x'],
         ['x','o','x','o']],

        [['x','o','x','x'],
         ['x','o','o','x'],
         ['x','x','o','x'],
         ['x','o','x','o']],

        [['x','x','x','x'],
         ['x','o','o','x'],
         ['x','o','o','x'],
         ['x','x','x','o']],

        np.array(['o', 'o', 'o', 'o', 'x', 'x', 'o', 'o', 'x', 'o', 'x', 'o', 'o', 'x', 'x', 'x', 'x', 'x', 'o', 'x', 'o', 'o', 'x', 'x', 'x', 'o', 'o', 'o']).reshape(4,7),

    ]
    inputs = [np.array(a) for a in inputs]
    for i in inputs:
        print(flip_x_o_recursive(i))
        print()