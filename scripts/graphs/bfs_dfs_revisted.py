
import collections

class Graph(object):

    def __init__(self):
        self.adj = collections.defaultdict(list)

    def add_edge(self, u, v):
        if v not in self.adj[u]:
            self.adj[u].append(v)

    def bfs_iterative(self, s):
        q = collections.deque()
        q.append(s)
        seen = set([s]) # start with seen including s
        order = []
        while len(q) > 0:
            cur = q.pop()
            order.append(cur)
            for neigh in self.adj[cur]:
                if neigh not in seen:
                    seen.add(neigh) # add to seen in the for loop
                    q.appendleft(neigh)
        return order

    def dfs_iterative(self, s):
        stack = [s]
        seen = set([s]) # start with seen including s
        order = []
        while len(stack) > 0:
            cur = stack.pop()
            order.append(cur)
            for neigh in self.adj[cur]:
                if neigh not in seen:
                    seen.add(neigh) # add to seen in the for loop
                    stack.append(neigh)
        return order

    def dfs_iterative_paths_broken(self, src, tgt):
        '''
        only prints the paths that don't share nodes other than src and tgt
        '''
        stack = [(src, [src])]
        seen = set([src]) # start with seen including s
        while len(stack) > 0:
            cur, path = stack.pop()
            for neigh in self.adj[cur]:
                if neigh == tgt:
                    yield path + [tgt]
                if neigh not in seen:
                    seen.add(neigh) # add to seen in the for loop
                    stack.append((neigh, path + [neigh]))

    def bfs_iterative_paths(self, src, tgt):
        q = collections.deque()
        q.append([src])
        while len(q) > 0:
            cur = q.pop()
            if cur[-1] == tgt:
                yield cur
            else:
                for neigh in self.adj[cur[-1]]:
                    if neigh not in cur:
                        q.appendleft(cur + [neigh])

if __name__ == '__main__':

    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'd')
    g.add_edge('b', 'c')
    g.add_edge('b', 'e')
    g.add_edge('b', 'f')
    g.add_edge('c', 'd')
    g.add_edge('c', 'g')
    g.add_edge('g', 'h')
    order = g.bfs_iterative('a')
    print(order)

    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'd')
    g.add_edge('a', 'e')
    g.add_edge('b', 'c')
    g.add_edge('e', 'f')
    order = g.bfs_iterative('a')
    print(order)
    order = g.dfs_iterative('a')
    print(order)

    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('b', 'd')
    g.add_edge('b', 'e')
    g.add_edge('e', 'f')
    g.add_edge('c', 'f')
    g.add_edge('d', 'e')
    paths = g.dfs_iterative_paths_broken('a', 'f')
    print(list(paths))
    paths = g.bfs_iterative_paths('a', 'f')
    print(list(paths))
    paths = g.dfs_recursive_paths('a', 'f')
    print(list(paths))
