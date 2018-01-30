'''
run bfs on valid spots keeping track of where we have reached so far
'''

import collections
import numpy as np

def neighbors(g, i, j):
    n, m = g.shape
    neighs = []
    for h in [-1,0,1]:
        for v in [-1,0,1]:
            if h == 0 and v == 0: 
                continue
            ni, nj = i+h, j+v
            if ni >= 0 and ni < n and nj >= 0 and nj < m and g[ni,nj] == 1:
                neighs.append((ni, nj))
    return neighs

def bfs(g,i,j):
    q = collections.deque()
    q.append((i,j))
    seen = set([(i,j)])
    while len(q) > 0:
        ci, cj = q.pop()
        for (ni, nj) in neighbors(g, ci, cj):
            if (ni,nj) not in seen:
                seen.add((ni,nj))
                q.appendleft((ni,nj))
    return list(seen)

def find_largest_ones(g):
    visited = np.zeros(g.shape, dtype=bool)
    n,m = g.shape
    maxsize = 0
    
    for i in range(n):
        for j in range(m):
            if g[i,j] == 1 and not visited[i,j]:
                reached = bfs(g,i,j)
                for (ri, rj) in reached:
                    visited[ri,rj] = True
                maxsize = max(maxsize, len(reached))
    return maxsize
      
if __name__ == '__main__':
    g = np.array([
        [1,1,0],
        [0,0,1],
        [1,0,1]
    ])
    maxsize = find_largest_ones(g)
    print(maxsize)