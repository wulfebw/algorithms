"""
:kerywords: sorting, mergesort, merge sort
"""

import copy

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

def merge_sort(lst):
    """
    :description: mergesort not in place

    :time: O(nlogn) this is (intuitively not mathematically) because if you break this problem down into a tree representation of the calls, you see that depth of that tree requires O(n) time and that there are logn depth levels in the tree giving a total run time of O(nlogn)
    :space: O(n), more precisely O(2n) since at the worst point we have to have double the size of the original list in memory (during the last call to merge)
    """
    if len(lst) <= 1:
        return lst
    cut = len(lst) / 2
    first = merge_sort(lst[:cut])
    second = merge_sort(lst[cut:])
    return merge(first, second)

if __name__ == '__main__':
    data = [[1,2,3],
            [1,3,4,6,8,67,5,43,2,2,34,6,6,6,74,3,2,3,4,4,54],
            [1],
            [4,3,2,1],
            [-4,-3,-5,-6, 5, 10]]

    overall = True
    for lst in data:
        sorted_data = merge_sort(copy.deepcopy(lst))
        print sorted_data
        result = sorted(lst) == sorted_data
        overall = overall and result
        print 'is the list sorted correctly?: {}'.format(result)
    print '\nwas everything correct?: {}'.format(overall)

"""
:additional notes:
- psuedocode for merge sort is 
    1. divide sequence into two n/2 length sequences
    2. conquer by recursively sorting these sequences with mergesort
    3. merge the sorted lists to get the final result

- sketch a proof that this is correct (from perspective of merge)
    1. initialization - first and second are sorted when they enter merge because they contain 1 element in the base case. So they at least start out sorted
    2. maintenance - merge goes through each appending only the value that is smallest of the two. When one of the lists runs out of elements, appends the rest of the other list, which from (1) we know is sorted.
    3. termination - at termination, we know that first and second come into the final call sorted and we know that (2) maintains this property, therefore merge must return a result that is sorted.
"""