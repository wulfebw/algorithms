
import collections

class Vertex(object):

    def __init__(self, k):
        self.k = k 
        self.p = None

    def __hash__(self):
        return hash(self.k)

    def __repr__(self):
        return 'vertex {}'.format(self.k)

    def __eq__(self, oth):
        '''
        when do you have to implement this?
        always because of collisions I think
        '''
        return self.k == oth.k


def neighbors(v, n, m):
    i,j = v.k
    # i plus minus 1 and j plus minus 2 
    indices = [
        (i+1,j+2),
        (i+1,j-2),
        (i-1,j+2),
        (i-1,j-2),
        (i+2,j+1),
        (i+2,j-1),
        (i-2,j+1),
        (i-2,j-1),
    ]
    neighs = []
    for ni, nj in indices:
        if ni >= 0 and ni < n and nj >= 0 and nj < m:
            neighs.append(Vertex((ni,nj)))
    return neighs

def knight_walk(src, dest, n, m):
    q = collections.deque()
    q.append(src)
    seen = set([src])

    found, cur = False, None
    while len(q) > 0:
        cur = q.pop()

        if cur == dest:
            found = True
            break

        else:
            for neigh in neighbors(cur, n, m):
                if neigh not in seen:
                    seen.add(neigh)
                    neigh.p = cur
                    q.appendleft(neigh)

    if found:
        # backtrack 
        path = []

        while cur.p is not None:
            path.append(cur)
            cur = cur.p 
        path.append(cur)
        return len(path) - 1

    else:
        return -1

if __name__ == '__main__':
    n, m = 4, 7
    src = Vertex((2-1,6-1))
    dest = Vertex((2-1,4-1))
    pathlen = knight_walk(src, dest, n, m)
    print(pathlen)

    n, m = 7, 13
    src = Vertex((2-1,8-1))
    dest = Vertex((3-1,4-1))
    pathlen = knight_walk(src, dest, n, m)
    print(pathlen)

    n, m = 3, 11
    src = Vertex((3-1,11-1))
    dest = Vertex((2-1,11-1))
    pathlen = knight_walk(src, dest, n, m)
    print(pathlen)