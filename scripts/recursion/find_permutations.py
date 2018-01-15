"""
Given list size m find all permutations size n.
"""

import itertools

def find_permutations(arr):
    # base case: if arr is length one then just return it
    if len(arr) <= 1:
        yield arr

    # otherwise, we need to find all the permutations 
    # do so by finding the permutations of the list
    # excluding the first element
    # assuming you have those permutations
    # then just insert back the first element of the 
    # array in each possible possition for each 
    # possible permutation
    else:
        for perm in find_permutations(arr[1:]):
            for i in range(len(arr)):
                yield perm[:i] + arr[0:1] + perm[i:]

if __name__ == '__main__':
    arr = [1,2,3,4]
    print(list(find_permutations(arr)))
    print(list(itertools.permutations(arr, 4)))