

import random

import m_queue
import representations

def print_path(g, s, v):
    """
    :description: prints the shortest path from v to s in g
    """
    if s == v:
        print s,
    elif v.pred == None:
        print 'no path from s to v'
    else:
        print_path(g, s, v.pred)
        print v,

def breath_first_search(g, s):
    """
    :description: breadth first search using vertex coloring

    :time: O(V + E)
    :space: O(?)
    """
    # create a queue to hold gray nodes
    q = m_queue.MyQueue(size=len(g))

    # add source to queue
    s.color = 'gray'
    s.dist = 0
    q.enqueue(s)

    # while there are nodes in the queue that have not been fully explored
    while not q.is_empty():

        # deqeue a node and go through its neighbors updating their info
        u = q.dequeue()
        for v in g[u]:
            if v.color == 'white':
                v.color = 'gray'
                v.pred = u
                v.dist = u.dist + 1
                q.enqueue(v)
        u.color = 'black'
    
if __name__ == '__main__':
    rand_adj_list = representations.build_random_adj_list(num_nodes=50)
    source = random.choice(rand_adj_list.keys())
    breath_first_search(rand_adj_list, source)
    dest = random.choice(rand_adj_list.keys())
    print '\n'
    print rand_adj_list
    print '\nsource: {}'.format(source)
    print 'dest: {}'.format(dest)
    print_path(rand_adj_list, source, dest)

"""
:additional notes:
- big takeways here are 
    1. bfs uses a queue to order its exploration of the state aka vertices
    2. it further uses some notion of how "known" those states are using a coloring scheme
"""
