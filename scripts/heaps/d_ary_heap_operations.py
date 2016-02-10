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

def print_heap(heap, d):
    print '\n'
    print heap[0]
    cur_depth = 0
    for idx, val in enumerate(heap[1:], 1):
        if cur_depth < int(math.log(idx, d)):
            cur_depth += 1
            print val
        else:
            print val,

if __name__ == '__main__':
    d = 4
    #A = [1,2,3,4,8,9,11]
    A = [3,4,5,6,5,4,5,6,1,2,3,4,5,6,5,4,3,2,1,11,3,4,5,6,7,8,9]
    build_max_heap(A, d)
    if is_valid_max_heap(A, d):
        print 'success: {} is a max heap'.format(A)
    else:
        print 'failure: {} not a max heap'.format(A)

    print_heap(A, d)







