

import random

import breadth_first_search
import m_queue
import representations

def depth_first_search(g, s):
    pass
    
if __name__ == '__main__':
    rand_adj_list = representations.build_random_adj_list(num_nodes=50)
    source = random.choice(rand_adj_list.keys())
    depth_first_search(rand_adj_list, source)
    dest = random.choice(rand_adj_list.keys())
    print '\n'
    print rand_adj_list
    print '\nsource: {}'.format(source)
    print 'dest: {}'.format(dest)
    breadth_first_search.print_path(rand_adj_list, source, dest)

"""
:additional notes:
"""
