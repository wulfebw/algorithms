
import random

import m_queue
import representations

def two_color(g, s, reds=set(), blues=set()):
    reds.add(s)
    q = m_queue.MyQueue(size=len(g))
    s.color = 'gray'
    q.enqueue(s)

    while not q.is_empty():
        u = q.dequeue()
        colorset = blues if u in reds else reds
        for v in g[u]:
            if v.color == 'white':
                v.color = 'gray'
                q.enqueue(v)
            colorset.add(v)
        del g[u]

    us = g.keys()
    if len(us) != 0:
        u = us[0]
        reds, blues = two_color(g, u, reds, blues)
        
    return reds, blues

def two_color_iter(g, s):
    """
    THIS DOESN'T WORK. WHY DOES IT NOT WORK?
    """
    reds = set()
    blues = set()
    for u, lst in g.iteritems():
        if u in reds:
            colorset = blues
        else:
            colorset = reds
            blues.add(u)

        for v in lst:
            colorset.add(v)

    return reds, blues

if __name__ == '__main__':
    rand_adj_list = representations.build_random_adj_list(num_nodes=1000)
    source = random.choice(rand_adj_list.keys())
    r1, b1 = two_color(rand_adj_list, source)
    #r2, b2 = two_color_iter(rand_adj_list, source)
    print rand_adj_list
    print '\n'
    print r1
    print b1
    print r1.intersection(b1)
    # print '\n'
    # print r2
    # print b2
    # print r2.intersection(b2)

