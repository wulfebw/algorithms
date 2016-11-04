
import heapq

class PriorityQueue(object):

    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def push(self, priority, value):
        heapq.heappush(self.heap, (priority, value))

    def pop(self):
        if not self.heap:
            raise ValueError("empty heap")
        return heapq.heappop(self.heap)