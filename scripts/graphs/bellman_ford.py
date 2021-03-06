
import numpy as np

class Vertex(object):

    def __init__(self, k):
        self.k = k
        self.reset()

    def reset(self):
        self.pi = None
        self.d = np.inf

    def __hash__(self):
        return hash(self.k)

    def __eq__(self, other):
        return self.k == other.k

    def __repr__(self):
        return str(self.k)

class Graph(object):

    def __init__(self, adj={}):
        self.adj = adj
        self.edges = set()
        for u, lst in self.adj.items():
            for v in lst:
                self.edges.add((u,v))

    def add_vertex(self, u):
        self.adj[u] = []

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.edges.add((u,v))

    def _initialize_single_source(self, s):
        '''
        Description:
            - set all vertices to have infinite path weight and nil predecessor
            except for the source, which has 0 path weight
        '''
        for k in self.adj.keys():
            k.reset()
        s.d = 0

    def _relax(self, u, v, w):
        '''
        Description:
            - if the current distance from s to v is greater than the distance 
            from s to u plus the distance from u to v, then use the path 
            containing u instead
        '''
        if v.d > u.d + w:
            v.d = u.d + w 
            v.pi = u

    def bellman_ford(self, w, s):
        '''
        Description:
            - run bellman-ford algorithm
            - each outer loop asks the question "can we do better by allowing 
            a path with 1 longer length?", and if the answer is yes it uses that 
            path

        Args:
            - w: dict mapping (u,v) pairs to weights 
            - s: vertex to use as source

        Returns:
            - true is no negative-weight cycle, else false
        '''
        self._initialize_single_source(s)

        for i in range(len(self.adj.keys()) - 1):
            for (u,v) in self.edges:
                self._relax(u,v,w[(u,v)])

        for (u,v) in self.edges:
            if v.d > u.d + w[(u,v)]:
                return False

        return True

    def shortest_path(self, s, t):
        path = [t]
        while t.pi is not None:
            path = [t.pi] + path
            t = t.pi 
        return path

def test_1():
    g = Graph()
    s = Vertex('s')
    a = Vertex('a')
    b = Vertex('b')
    vs = [s,a,b]
    for v in vs:
        g.add_vertex(v)
    
    es = [
        (s,a),
        (s,b),
        (b,a)
    ]
    for e in es:
        g.add_edge(*e)

    w = {
        (s,a): 10,
        (s,b): 1,
        (b,a): 1,
    }

    valid = g.bellman_ford(w, s)
    print(valid)
    print(g.shortest_path(s,a))
    print(g.shortest_path(s,b))


if __name__ == '__main__':
    test_1()