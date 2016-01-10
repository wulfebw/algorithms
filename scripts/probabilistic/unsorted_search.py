"""
:keywords: probability, searching
"""

import random

import random_permutation

def random_search(arr, val):
    """
    :description: searches an array for a value by randomly selecting indicies and check for the value at that location

    :time: average case O(n) - geometric distribution with success probability 1/n, which has expected value of n (normally geometric has success probability p with mean 1/p). Of course the worst case runtime is, I guess infinite because it's possible that an index is never randomly selected. You could probably give a more meaningful analysis of the worst case. Something like with probability 1 - delta though.
        Actually, the above assumes only one instance of the value to be found. Generally, if there are k repetitions of the value, over len n array, then the probability is k/n of randomly selecting the element so the average case is O(n/k)
        Also can consider the average case if the element is not in the array. In that situation, it is a question of how many random indicies must you select on average in order to select every index. 
    :space: O(n)
    """
    indicies = set()
    size = len(arr)
    while True:
        if len(indicies) == size:
            return -1
        index = random.randint(0, size - 1)
        indicies.add(index)
        if arr[index] == val:
            return index


def linear_search(lst, val):
    """
    :description: linear searching algorithm 

    :time: O(n) - goes through each element once. Average case run time is (n+1)/(k+1). Need to derive that
    :space: O(1) - don't count the input list, just have an index 
    """
    for idx, ele in enumerate(lst):
        if ele == val:
            return idx
    return -1

def scramble_search(lst, val):
    """
    :description: randomly permutes the list and then runs linear search
    """
    lst = random_permutation.random_permutation_swap(lst)
    return linear_search(lst, val)

if __name__ == '__main__':
    data = [[1,2,3],
            [1,2,3,4,5,6,7],
            [-5,-4,-3,-2,-1,0,1,2,3,4,5],
            [1],
            [1, 1000],
            [1, 1000, 1000000]]
    vals = [3,4,-2,0,1000,1000]
    overall = True
    for lst, val in zip(data, vals):
        index = scramble_search(lst, val)
        if index >= 0:
            print 'found at index: {}'.format(index)
        else:
            print 'value not in list'
        pyidx = lst.index(val) if val in lst else -1
        result = index == pyidx
        overall = overall and result
        print 'was the value found correctly?: {}'.format(result)
    print '\nall tests correct?: {}'.format(overall)

"""
:additional notes:

- three methods
    1. random search
    2. linear search
    3. scramble search
- which to use?
    - depends (actually doesn't just always use linear search)
    - linear search is probably fine in general 
    - if you know the input is antagonistic is it better to use scramble search?
        - don't think so because the scrambling part takes O(n), and in fact always takes ~n operations
        - the linear search might be sped up, but it at most uses ~n operations alone, so wouldn't you then be better off using just linear search always?

"""