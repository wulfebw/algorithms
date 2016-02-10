"""
:description: d-ary heap implementation
"""

import math

def parent(i, d):
    return max((i - 1) / d, 0)

def children_indices(i, d):
    return range(i * d + 1, i * d + d + 1)

def max_heapify(A, i, d):
    """
    :description: recursively enforces the heap property by comparing a node in index i of the array with its left and right children (left(i) and right(i)). If one of the children is larger, it swaps i with the larger child and then calls max_heapify on the location where that larger child used to be (i.e., it calls max_heapify on i again). The result is that i moves down the heap in only O(lgn) time complexity because it will at most travel down lgn times.

    :time: O(lgn) because for any index i in array A, max_heapify will at most be called recursively lgn times (at that point you will be at the bottom of the tree). Each call to max_heapify has an immediate cost of O(1)

    :space: O(1)
    """
    largest = i
    for child_idx in children_indices(i, d):
        if child_idx < len(A) and A[child_idx] > A[largest]:
            largest = child_idx

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, d)

def build_max_heap(A, d):
    """
    :description: given an array A, builds a max heap by recursively calling max_heapify

    :time: O(n) due to the fact that most nodes considered have relatively low height in the tree (pg 159 for actual math). Only call on first half of array since the second half does not have children (this point really emphasizes the fact that most of the nodes in a tree are in the bottom layer (half, actually))

    :space: O(1)
    """
    for i in reversed(range(0, len(A))):
        max_heapify(A, i, d)

def is_valid_max_heap(A, d):
    for i in range(0, len(A)):
        if A[i] > A[parent(i, d)]:
            return False
    return True

def heap_extract_max(heap, d):
    """
    :description: remove and return the max value while maintaining the max heap property

    :time: O(lgn)
    """
    assert len(heap) > 0

    heap[0], heap[-1] = heap[-1], heap[0]
    max_value = heap.pop()
    max_heapify(heap, 0, d)
    return max_value


def heap_increase_key(heap, i, new_value, d):
    """
    :description: increase the value of a key and subsequently ensure max heap property is maintained

    :time: O(lgn) because moving the element with the new value to the top of the tree requires at most lgn operations
    """
    assert new_value > heap[i]

    heap[i] = new_value
    while heap[i] > heap[parent(i, d)]:
        heap[i], heap[parent(i, d)] = heap[parent(i, d)], heap[i]
        i = parent(i, d)

def max_heap_insert(heap, value, d):
    """
    :description: insert an element into the heap 

    :time: O(lgn)
    """
    heap.append(-sys.maxint)
    heap_increase_key(heap, len(heap) - 1, value, d)

if __name__ == '__main__':
    d = 4
    #A = [1,2,3,4,8,9,11]
    A = [3,4,5,6,5,4,5,6,1,2,3,4,5,6,5,4,3,2,1,11,3,4,5,6,7,8,9]
    build_max_heap(A, d)
    if is_valid_max_heap(A, d):
        print 'success: {} is a max heap'.format(A)
    else:
        print 'failure: {} not a max heap'.format(A)


    heap_extract_max(A, d)
    if is_valid_max_heap(A, d):
        print 'success: {} is a max heap'.format(A)
    else:
        print 'failure: {} not a max heap'.format(A)








