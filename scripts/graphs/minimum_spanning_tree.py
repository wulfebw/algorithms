'''
prims implementation using binary heap 
    - put all the vertices into a min queue 
    - extract them one by one 
        + each time updating nodes connected to the extracted one still in the q 
    - when you extarct all the nodes you're finished 
    - some tricky things about this 
        1. you have to keep track of the indices of each vertex in the min heap in the q
            - so as to allow for fast update + min_heapify of nodes 
            - these updates have to be performed in the min q
        2. you also have to track whether the node is in the q 

applications of minimum spanning tree
    - if you're aksed to connect a set of nodes s.t., the total edge weights in 
    the connected graph is minimal use the minimum spanning tree algorithm
    - primary other application is for approximating np-hard problems 
        - traveling salesman 
        - steiner trees
'''
import functools
import sys

sys.path.append('../heaps')
import min_priority_queue

@functools.total_ordering
class Vertex(object):

    def __init__(self, k, w=np.inf, p=None, in_q=True, index=None):
        self.k = k
        self.value = w 
        self.p = p 
        self.in_q = in_q
        self.index = None

    def set_index(self, index):
        self.index = index

    def set_value(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value 

    def __lt__(self, other):
        return self.value < other.value

def prims(g, w, r):
    vertices = []
    for k in g.keys():
        vertices.append(Vertex(k))
    q = min_priority_queue.MinPriorityQueue(vertices)
    q.decrease_index(r.index, 0)

    while not q.empty():
        u = q.pop()
        for v in g[u.k]:
            # if by adding u to the MST, we decrease the light edge connecting 
            # the tree to v, then decrease the weight to v accordingly
            if v.in_q and w[u.k,v.k] < v.value:
                v.p = u
                q.decrease_index(v.index, w[u.k,v.k])


 