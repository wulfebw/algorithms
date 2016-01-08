"""
:keywords: merge sort, insertion sort, sorting
"""

import copy

import insertion_sort

### Not inplace #################################
def merge(first, second):
    i1 = 0
    i2 = 0
    result = []
    while i1 < len(first) and i2 < len(second):
        if first[i1] < second[i2]:
            result.append(first[i1])
            i1 += 1
        else:
            result.append(second[i2])
            i2 += 1
    if i1 >= len(first):
        result += second[i2:]
    else:
        result += first[i1:]
    return result

def merge_insertion_sort(lst, k=2):
    """
    :description: mergesort not in place

    :time: O(nlogn) this is (intuitively not mathematically) because if you break this problem down into a tree representation of the calls, you see that depth of that tree requires O(n) time and that there are logn depth levels in the tree giving a total run time of O(nlogn)
    :space: O(n), more precisely O(2n) since at the worst point we have to have double the size of the original list in memory (during the last call to merge)
    """
    if len(lst) <= k:
        return insertion_sort.insertion_sort(lst)
    cut = len(lst) / 2
    first = merge_insertion_sort(lst[:cut])
    second = merge_insertion_sort(lst[cut:])
    return merge(first, second)

if __name__ == '__main__':
    data = [[1,2,3],
            [1,3,4,6,8,67,5,43,2,2,34,6,6,6,74,3,2,3,4,4,54],
            [1],
            [4,3,2,1],
            [-4,-3,-5,-6, 5, 10]]

    overall = True
    for lst in data:
        sorted_data = merge_insertion_sort(copy.deepcopy(lst))
        print sorted_data
        result = sorted(lst) == sorted_data
        overall = overall and result
        print 'is the list sorted correctly?: {}'.format(result)
    print '\nwas everything correct?: {}'.format(overall)

"""
:additional notes: 
1. show insertion sort can sort n/k lists of len k in O(nk) - sorting len k list takes k^2 there are n/k giving O(k^2 * n/k) = O(nk)
2. show merge in O(nlog(n/k)) - each layer requires n operations there are log(n/k) layers

- the difference from merge sort is that instead of returning when len == 1, return the sorted list when length == k
"""


