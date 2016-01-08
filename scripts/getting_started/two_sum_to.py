"""
:keywords: sorting, summing
"""

import timeit

import numpy as np

import binary_search

def two_sum_to_iterate(lst, val):
    """
    :description: determines whether any two numbers in a set add to a given value
        this doesnt find all such values

    :time: O(nlogn) - sorting in nlogn but the finding takes O(n)
    :space: O(1)

    :execution: running run 10000 times in 16.1 seconds
    """
    at_least_one = False
    found = False
    lst = sorted(lst)
    idx1 = 0
    idx2 = len(lst) - 1
    while idx1 < idx2:
        total = lst[idx1] + lst[idx2]
        if total == val:
            return True
        elif total < val:
            idx1 += 1
        else:
            idx2 -= 1

    return False

def two_sum_to_search(lst, val):
    """
    :description: finds all pairs of values that add to the value using binary search on the 
        difference between the value and each item

    :time: O(nlogn) - sorting in nlogn, finding in O(logn)
    :space: O(1)

    :execution: running run 10000 times in 16.1 seconds
    """
    found = False
    lst = sorted(lst)
    for i, x in enumerate(lst):
        j = binary_search.binary_search(lst, val - x)
        if j != -1:
            print 'pair: {} {}'.format(i,j)
            found = True
    return found

def two_sum_to_hash(lst, val):
    """
    :description: finds all pairs by hashing them and then search for the hash of the difference 

    :time: O(n) to hash O(n) to lookup
    :space: O(n) to store the hash table

    :execution: running run 10000 times in 12.3 seconds
    """
    found = False
    d = dict()
    for i, x in enumerate(lst):
        d[x] = i

    for i, x in enumerate(lst):
        diff = val - x 
        if diff in d:
            print 'pair: {} {}'.format(i, d[diff])
            found = True
    return found

def run():
    data = [list(set([1,2,3])),
            list(set([1,2,3,4,5,6,7])),
            list(set([-5,-4,-3,-2,-1,0,1,2,2,4,5])),
            list(set([1])),
            list(set([1, 1000])),
            list(set([1, 1000, 1000000]))]
    vals = [4,8,-2,0,1001,1000]
    actuals = [True, True, True, False, True, False]
    overall = True
    for lst, val, actual in zip(data, vals, actuals):
        found = two_sum_to_iterate(lst, val)
        if found:
            print 'found'
        else:
            print 'not found'
        result = found == actual
        overall = overall and result
        print 'was the value found correctly?: {}'.format(result)
    print '\nall tests correct?: {}'.format(overall)

if __name__ == '__main__':
    t = timeit.Timer(run)
    print(t.timeit(number=10000))


"""
:additional notes:
"""