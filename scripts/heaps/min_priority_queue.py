'''
this implementation is specifically for pimm's MST algorithm
'''
import numpy as np

def parent(i):
    return max((i - 1) / 2, 0)

def left(i):
    return i * 2 + 1

def right(i):
    return i * 2 + 2

def min_heapify(A, i):
    l, r = left(i), right(i)
    smallest = i

    if l < len(A) and A[l] < A[smallest]:
        smallest = l

    if r < len(A) and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[i].set_index(smallest)
        A[smallest].set_index(i)

        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)

def build_min_heap(h):
    for i in reversed(range(0, len(h) / 2 + 1)):
        min_heapify(h, i)

def heap_extract_min(h):
    assert len(h) > 0

    h[0].set_index(-1)
    h[-1].set_index(0)

    h[0], h[-1] = h[-1], h[0]
    min_value = h.pop()
    min_value.in_q = False
    min_heapify(h, 0)
    return min_value

def heap_decrease_key(h, i, new_value):
    assert new_value < h[i].value
    h[i].set_value(new_value)

    while h[i] < h[parent(i)]:
        # update indices of nodes
        h[i].set_index(parent(i))
        h[parent(i)].set_index(i)

        h[i], h[parent(i)] = h[parent(i)], h[i]
        i = parent(i)

class MinPriorityQueue(object):

    def __init__(self, h=[]):
        self.h = build_min_heap(h)
        self.size = len(h)

    def pop(self):
        self.size -= 1
        return heap_extract_min(self.h)

    def decrease_index(self, i, w):
        heap_decrease_key(self.h, i, w)

    def empty(self):
        return self.size <= 0 
