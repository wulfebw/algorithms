
import collections
import heapq
import Queue
import sys
import timeit

class PriorityHeap(object):

    def __init__(self):
        self.heap = []

    def put(self, val):
        if val not in self.heap:
            heapq.heappush(self.heap, val)

    def get(self):
        return heapq.heappop(self.heap)

    def empty(self):
        return len(self.heap) <= 0

def uniform_cost_search(adj_list, source, dest):
    """
    :description: NOT WORKING YET uniform cost search. only works if there are no negative edge weights
    """

    frontier = PriorityHeap()
    frontier.put((adj_list[source]['d'], source))
    explored = []

    while not frontier.empty():

        d, cur = frontier.get()

        if cur == dest:
            break

        explored.append(cur)

        for vertex, weight in adj_list[cur].iteritems():
            if vertex != 'd' and vertex != 'pi' and vertex not in explored:
                explored.append(vertex)

                frontier.put((adj_list[cur]['d'] + adj_list[cur][vertex], vertex))

        # for vertex, verticies in adj_list.iteritems():
        #     if cur in verticies:
        #         new_dist = adj_list[vertex]['d'] + adj_list[vertex][cur]
        #         if new_dist < adj_list[cur]['d']:
        #             adj_list[cur]['d'] = new_dist
        #             adj_list[cur]['pi'] = vertex

        # if cur == dest:
        #     break

    path = None
    if adj_list[dest]['pi'] is not None:
        path = [dest]
        while path[-1] != source:
            predecessor = adj_list[path[-1]]['pi']
            path.append(predecessor)
        path = list(reversed(path))
    return path, adj_list[dest]['d']

def breadth_first_search_shortest_path(adj_list, source, dest):
    """
    :description: BFS, only works if you assume all the weight costs are 1 
    """

    frontier = Queue.Queue()
    frontier.put(source)

    while not frontier.empty():

        cur = frontier.get()
        for vertex, weight in adj_list[cur].iteritems():
            if vertex != 'd' and vertex != 'pi':
                frontier.put(vertex)
                if adj_list[cur]['d'] + adj_list[cur][vertex] < adj_list[vertex]['d']:
                    adj_list[vertex]['d'] = adj_list[cur]['d'] + adj_list[cur][vertex]
                    adj_list[vertex]['pi'] = cur
        if cur == dest:
            break

    path = None
    if adj_list[dest]['pi'] is not None:
        path = [dest]
        while path[-1] != source:
            path.append(adj_list[path[-1]]['pi'])
        path = list(reversed(path))
    return path, adj_list[dest]['d']

def init_single_source(adj_list, source):
    """
    :description: when you are using an adjacency list and your goal is to find the shortest path, you need a way to keep track of what the current min path cost to a vertex is and what predecessor provides that path. To do this you track exactly that information: the distance d (initialized to inf) and the predecessor pi (initialized to None). 

        This answers the question "how do you track the minimum path to a point and how did you get there".
    """
    for v, edge_dict in adj_list.iteritems():
        edge_dict['d'] = sys.maxint
        edge_dict['pi'] = None
    adj_list[source]['d'] = 0

def get_adj_list():
    adj_list = collections.defaultdict(lambda: collections.defaultdict(lambda: sys.maxint))
    adj_list['A']['B'] = 1
    adj_list['A']['C'] = 2
    adj_list['A']['D'] = 4
    adj_list['B']['E'] = 7
    adj_list['B']['C'] = 3
    adj_list['C']['E'] = 1
    adj_list['D']['E'] = 5
    adj_list['D']['E'] = 2
    adj_list['D']['F'] = 10
    adj_list['D']['I'] = 7
    adj_list['I']['A'] = 7
    adj_list['E']['H'] = 8
    adj_list['E']['G'] = 12
    adj_list['E']['L'] = 1000
    adj_list['F']['G'] = 1
    adj_list['H']['G'] = 1
    adj_list['H']['G'] = 1
    adj_list['H']['E'] = 2
    adj_list['G']['I'] = 4
    adj_list['G']['E'] = 7
    adj_list['G']['C'] = 3
    adj_list['I']['J'] = 1
    adj_list['I']['K'] = 5
    adj_list['I']['E'] = 2
    adj_list['J']['L'] = 1
    adj_list['J']['I'] = 7
    adj_list['J']['K'] = 7
    adj_list['K']['H'] = 3
    adj_list['K']['I'] = 2
    adj_list['K']['G'] = 1
    adj_list['K']['L'] = 1
    init_single_source(adj_list, 'A')
    return adj_list, 'A', 'L'

def run_bfs():
    adj_list, source, dest = get_adj_list()
    shortest_path = breadth_first_search_shortest_path(adj_list, source, dest)
    print shortest_path

def run_ucs():
    adj_list, source, dest = get_adj_list()
    shortest_path = uniform_cost_search(adj_list, source, dest)
    print shortest_path

if __name__ == '__main__':
    t = timeit.Timer(run_bfs)
    print(t.timeit(number=1))
    t = timeit.Timer(run_ucs)
    print(t.timeit(number=1))