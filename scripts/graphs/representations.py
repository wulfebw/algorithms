
import collections
import numpy as np
import random
import sys

class Vertex(object):

    def __init__(self, name=None):
        self.name = name
        self.color = 'white'
        self.pred = None
        self.dist = sys.maxint

    def __repr__(self):
        return str(self.name)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.name)

def build_random_adj_mat(nodes):
    adj_mat = np.random.randn(nodes, nodes)
    adj_mat[adj_mat > 0] = 1
    adj_mat[adj_mat <= 0] = 0
    return adj_mat

def build_random_adj_list(num_nodes, max_edges=2):
    nodes = {idx: Vertex(name=idx) for idx in range(num_nodes)}

    adj_list = collections.defaultdict(lambda: set())
    for node in range(num_nodes):
        v = nodes[node]
        neighbors = np.random.choice(range(num_nodes), random.randint(0, max_edges), replace=False)
        for name in neighbors:
            if name != node:
                neighbor = nodes[name]
                adj_list[v].add(neighbor)
                adj_list[neighbor].add(v)

    return adj_list

if __name__ == '__main__':
    adj_list = build_random_adj_list(num_nodes=5)
    print adj_list
    adj_mat = build_random_adj_mat(num_nodes=5)
    print adj_mat


