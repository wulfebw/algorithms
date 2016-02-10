
def parent(i):
    return max((i - 1) / 2, 0)

def left(i):
    return i * 2 + 1

def right(i):
    return i * 2 + 2

def max_heapify(A, i):
    """
    :description: recursively enforces the heap property by comparing a node in index i of the array with its left and right children (left(i) and right(i)). If one of the children is larger, it swaps i with the larger child and then calls max_heapify on the location where that larger child used to be (i.e., it calls max_heapify on i again). The result is that i moves down the heap in only O(lgn) time complexity because it will at most travel down lgn times.

    :time: O(lgn) because for any index i in array A, max_heapify will at most be called recursively lgn times (at that point you will be at the bottom of the tree). Each call to max_heapify has an immediate cost of O(1)

    :space: O(1)
    """
    l, r = left(i), right(i)
    largest = i

    if l < len(A) and A[l] > A[largest]:
        largest = l

    if r < len(A) and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    """
    :description: given an array A, builds a max heap by recursively calling max_heapify

    :time: O(n) due to the fact that most nodes considered have relatively low height in the tree (pg 159 for actual math). Only call on first half of array since the second half does not have children (this point really emphasizes the fact that most of the nodes in a tree are in the bottom layer (half, actually))

    :space: O(1)
    """
    for i in reversed(range(0, len(A) / 2 + 1)):
        max_heapify(A, i)

def is_valid_max_heap(A):
    for i in range(0, len(A)):
        if A[i] > A[parent(i)]:
            return False
    return True


if __name__ == '__main__':
    A = [1,2,3,4,5,6]
    A = [3,4,5,6,5,4,5,6,1,2,3,4,5,6,5,4,3,2,1,11,3,4,5,6,7,8,9]
    build_max_heap(A)
    if is_valid_max_heap(A):
        print 'success: {} is a max heap'.format(A)
    else:
        print 'failure: {} not a max heap'.format(A)