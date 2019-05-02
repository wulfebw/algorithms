import collections
import sys

class Vertex(object):
    
    def __init__(self, k):
        self.k = k
        self.pi = None
        self.d = sys.maxsize
        self.color = 'white'
        
    def __hash__(self):
        return hash(self.k)
    
    def __eq__(self, other):
        return self.k == other.k
    
    def __repr__(self):
        return str(self.k)
        
class Graph(object):
    
    def __init__(self, adj):
        self.adj = adj
        
    def successors(self, u):
        return self.adj[u]
    
def build_knight_graph(n,a,b):
    vertices = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            vertices[i][j] = Vertex((i,j))
            
    adj = dict()
    for i in range(n):
        for j in range(n):
            neigh = set()

            if i + a < n and j + b < n:
                neigh.add(vertices[i+a][j+b])
            if i + a < n and j - b >= 0:
                neigh.add(vertices[i+a][j-b])
            if i - a >= 0 and j + b < n:
                neigh.add(vertices[i-a][j+b])
            if i - a >= 0 and j - b >= 0:
                neigh.add(vertices[i-a][j-b])
            if i + b < n and j + a < n:
                neigh.add(vertices[i+b][j+a])
            if i + b < n and j - a >= 0:
                neigh.add(vertices[i+b][j-a])
            if i - b >= 0 and j + a < n:
                neigh.add(vertices[i-b][j+a])
            if i - b >= 0 and j - a >= 0:
                neigh.add(vertices[i-b][j-a])
            adj[vertices[i][j]] = list(neigh)
    g = Graph(adj)
    s = vertices[0][0]
    t = vertices[n-1][n-1]
    return g, s, t

def get_path(u):
    path = []
    while u is not None:
        path = [u] + path
        u = u.pi
    return path
         
def min_knight_path(g, s, t):
    s.color = 'gray'
    s.d = 0
    q = collections.deque([s])
    
    while len(q) > 0:
        u = q.pop()
        
        if u == t:
            return t.d, get_path(t)
        else:
            for v in g.successors(u):
                if v.color == 'white':
                    v.color = 'gray'
                    v.pi = u
                    v.d = u.d + 1
                    q.appendleft(v)
        u.color = 'black'
                           
    return -1, []
        
n = int(input().strip())
min_steps = [[-1 for _ in range(n-1)] for _ in range(n-1)]

for a in range(1, n):
    for b in range(1, n):
        g, s, t = build_knight_graph(n,a,b)    
        min_steps[a-1][b-1], _ = min_knight_path(g, s, t)
        sys.stdout.write(str(min_steps[a-1][b-1]) + ' ')
    print()