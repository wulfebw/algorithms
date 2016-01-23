import heapq

import numpy as np

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

def ucs(image):
    heap = PriorityHeap()

    for i, val in enumerate(image[:, 0]):
        heap.push((val, (i, 0)))

def run():
    image = [[1,2,3],
            [3,2,1],
            [1,1,5],
            [5,1,1]]
    image = np.array(image)
    shortest_path = ucs(image)
    print shortest_path

if __name__ =='__main__':
    run()