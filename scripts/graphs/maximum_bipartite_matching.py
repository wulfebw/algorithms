'''
ok outline of ff 
1. build regular graph 
2. build residual graph 
3. find shortest s-t path in residual graph 
4. increment / decrement forward / reverse edges in original graph 
5. repeat until no s-t path exists
'''
import collections 
import numpy as np

class Vertex(object):

    def __init__(self, k):
        self.k = k
        self.p = None

    def __hash__(self):
        return hash(self.k)

class Edge(object):

    def __init__(self, src, dest, u, forward=True):
        self.src = src 
        self.dest = dest 
        self.u = u 
        self.t = 0
        self.forward = forward

class Graph(object):

    def __init__(self, src, tgt):
        self.adj = collections.defaultdict(list)
        self.edges = {}
        self.src = src
        self.tgt = tgt

    def add_edge(self, e):
        if e.dest not in self.adj[e.src]:
            self.adj[e.src].append(e.dest)
        self.edges[(e.src, e.dest)] = e

    def build_residual(self):
        g = Graph()
        for edge in self.edges():
            d = edge.u - edge.f 
            if d > 0:
                g.add_edge(edge.src, edge.tgt, d, True)
            if edge.f > 0:
                g.add_edge(edge.tgt, edge.src, edge.f, False)
        return g

    def flow(self):
        total = 0
        for edge in self.edges:
            if edge.dst == self.tgt:
                total += edge.f
        return total 

    def bfs(self, g):
        '''
        return the shortest path (in hops) from g.src to g.dest
        '''
        q = collections.deque()
        q.append(g.src)
        seen = set([g.src])
        while len(q) > 0:
            cur = q.pop()
            if cur == g.tgt:
                break
            for neigh in g.adj[cur]:
                if neigh not in seen:
                    neigh.p = cur
                    seen.add(neigh)
                    q.appendleft(neigh)

        # get the path:
        path = []
        while cur.p != q.src:
            path.append(cur)
            cur = cur.p
        return [q.src] + path 
                    
    def ford_fulkerson(self):
        while True:

            # build residual graph 
            res = self.build_residual()

            # runs bfs to find shortest path 
            # sequence of vertices
            path = self.bfs(res)
            if path is None:
                break

            # compute delta
            delta = min([res.edges[v].u - res.edges[v].f for v in path])

            # increment / decrement forward / reverse edges 
            for src, dest in zip(path, path[1:]):
                e = res.edges[(src,dest)]
                if e.forward:
                    self.edges[(src, dest)].f += delta
                else:
                    self.edges[(dest, src)].f -= delta

        return flow()


