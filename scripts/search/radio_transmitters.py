'''
This is actually a simple greedy problem, but requires a linear search 
with a bit of backtracking
'''

'''
find minimum number of radio towers to connect houses
'''

def incorrect_solution(x,k):
    if len(x) == 0: return 0
    if len(x) == 1: return 1

    to_cover = x[0]
    count = 0
    for i in range(1, len(x)):
        if x[i] - k > to_cover:
            count += 1
            to_cover = x[i-1] + k 
    if to_cover < x[-1]:
        count += 1
    return count

def find_component_edges(x,k):
    edges = []
    s = 0
    for i in range(1, len(x)):
        if x[i] - x[i-1] > k:
            edges.append((s,i-1))
            s = i
    edges.append((s, len(x)-1))
    return edges

def compute_component_min_edges(x,k,s,e):
    return incorrect_solution(x[s:e+1],k)

def another_greedy_solution(x,k):
    x = list(set(x))
    x.sort()
    count = 0
    component_edges = find_component_edges(x,k)
    for (s,e) in component_edges:
        count += compute_component_min_edges(x,k,s,e)
    return count

def hackerlandRadioTransmitters(x,k):
    return another_greedy_solution(x,k)

# class Vertex(object):

#     def __init__(self, k):
#         self.k = k

# class Edge(object):

#     def __init__(self, u, v, w):
#         self.u = u 
#         self.v = v 
#         self.w = w

# class Graph(object):

#     def __init__(self, adj={}):
#         self.adj = adj

#     def prims(self, s):
#         # put all edges in a priority queue
#         # their weight is the minimum cost of connecting them to the current mst
#         # so for all edges not connected to s that's infinity
#         # for edges connected to s that's 

#         # repeat until all nodes connected
#         # pop lowest priority edge
#         # add it to the mst graph 
#         # for each edge connected to the node added 
#         pass

#     def mst(self):
#         # select a starting node
#         vs = self.adj.keys()
#         if len(vs) == 0:
#             return Graph()

#         s = vs[0]
#         return self.prims(s)

# def build_radio_graph(x,k):
#     return None

# def hackerlandRadioTransmitters(x,k):
#     # build graph
#     g = build_radio_graph(x, k)

#     # find mst
#     mst = g.mst()

#     # return number of edges
#     return mst.num_edges


if __name__ == '__main__':
    x = [0,1,2,4,5,6,10,11,12]
    k = 1
    result = hackerlandRadioTransmitters(x,k)
    print(result)


    x = [2,2,2,2,1,1,1,1]
    k = 2
    result = hackerlandRadioTransmitters(x,k)
    print(result)
    
    x = [10,10,10]
    k = 3
    result = hackerlandRadioTransmitters(x,k)
    print(result)