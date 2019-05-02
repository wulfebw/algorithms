'''
for each set of vertices that can be connected, choose the cheapest library to 
build and build it 
then find the mst for that set of components

how does prims work again?
- it starts with an unconnected graph 
- then selects the edge that will connect the mst to a new vertex that also costs the least
    + for this to work, it would mean that each time a vertex is added you have change the cost for a bunch of vertices
- is it something else instead?
    + maybe it's you keep the vertices in the priority queue?
        * this would work slightly more easily
    + ok, you keep the vertices
'''

from minimum_spanning_tree import prims, Vertex

if __name__ == '__main__':

    g = {}
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')





