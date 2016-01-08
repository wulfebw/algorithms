"""
:keywords: maximum sub array, divide and conquer
"""

import copy

def max_subarray_naive(arr):
    """
    :description: basic algo for finding max sub array which just goes through all sub arrays

    :time: O(n^3)
    :space: O(1)
    """
    if len(arr) == 0:
        return arr

    if len(arr) == 1:
        if sum(arr) > 0:
            return arr
        else:
            return []

    max_total = arr[0]
    best_start = -1
    best_finish = -1
    for start, _ in enumerate(arr):
        for finish, _ in enumerate(arr[start:], start + 1):
            total = sum(arr[start: finish])

            if total > max_total:
                max_total = total
                best_start = start
                best_finish = finish

    return arr[best_start:best_finish]

def max_subarray_divide_and_conquer(arr):
    """
    :description: divide and conquer style max sub array. The max subarray is either in the range start:mid, mid:finish, or crosses the mid value.

    :time: O(nlogn) (at least it should be nlogn but the max_cross_naive is O(n^2))
    :space: O(1)
    """

    if len(arr) < 1:
        return []
    
    def max_cross_naive(arr, start, finish, mid):
        left_total, sidx = max((sum(arr[s: mid]), s) for s in range(start, mid+1))
        right_total, fidx = max((sum(arr[mid: f]), f) for f in range(mid, finish+1))
        return left_total + right_total, sidx, fidx

    def recurse(arr, start, finish):
        if len(arr[start:finish]) == 1:
            return arr[start], start, finish

        mid = (finish - start) / 2 + start
        return max(recurse(arr, start, mid),
                recurse(arr, mid, finish),
                max_cross_naive(arr, start, finish, mid))

    total, s, f = recurse(arr, 0, len(arr))
    return arr[s:f]

def max_subarray_linear(arr):
    """
    :description: linear max sub array, Kadane's

    :time: O(n)
    :space: O(1)
    """
    max_so_far = 0
    max_ending_here = 0
    cur_start = -1
    best_start = -1
    end = -1
    for i, x in enumerate(arr):
        if max_ending_here == 0 and x > 0:
            cur_start = i
        max_ending_here = max(0, max_ending_here + x)

        if max_ending_here > max_so_far:
            end = i
            best_start = cur_start
        max_so_far = max(max_so_far, max_ending_here)
    return arr[best_start: end+1]

def max_subarray_strassens(arr):
    raise NotImplementedError("don't think there's much value in this")

if __name__ == '__main__':
    data = [[-1,1,-1],
            [1,2,3,-1,-2,-3],
            [1,3,4,6,8,67,5,43,2,2,34,6,6,6,74,3,2,3,4,4,54],
            [1,2,3,4,0,-1],
            [4,3,2,1,-2,-5,1000],
            [-10,4,3,2,1,-2,-5,1],
            [-4,-3,-5,-6,5,10],
            [],
            [1],
            [-1,-2,-3,-4,0]]
    maximum_arrays = [
                [1],
                [1,2,3],
                [1,3,4,6,8,67,5,43,2,2,34,6,6,6,74,3,2,3,4,4,54],
                [1,2,3,4],
                [4,3,2,1,-2,-5,1000],
                [4,3,2,1],
                [5,10],
                [],
                [1],
                []]

    overall = True
    for lst, actual in zip(data, maximum_arrays):
        max_array = max_subarray_linear(lst)
        print max_array
        result = max_array == actual
        overall = overall and result
        print 'correct max subarray?: {}'.format(result)
    print '\nwas everything correct?: {}'.format(overall)

"""
:additional notes: 
- enumerating in the inner loop - if you want to start from a location use enumerate(list, start_index)
- when recursing with a midpoint, be explicit about how that midpoint is defined - is it the middle element or is it separating between two elements?
- if a problem seems like it might be solvable in some more efficient way, consider what structure in the problem would allow you to take greedy actions
- also try dynammic programming
"""


