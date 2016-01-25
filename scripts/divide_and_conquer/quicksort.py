"""
:kerywords: sorting, quicksort, quick sort
"""

import copy
import random

def tail_recursion_quicksort(arr, random_ordering=False):
    """
    :description: version of quicksort that only makes a single recursive call by first sorting the left half of the array (as determined by the initial pivot location) and then sorting the right half (of which it's left half is sorted first, continuing until there are no elements in the right half).
    """

    def partition(arr, start, end):
        i = start - 1
        for j in range(i + 1, end):
            if arr[j] < arr[end]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
        arr[i], arr[end] = arr[end], arr[i]
        return i
    
    def recurse(arr, start, end):
        while start < end:
            pivot = partition(arr, start, end)
            recurse(arr, start, pivot - 1)
            start = pivot + 1

    recurse(arr, 0, len(arr) - 1)
    return arr

def quicksort(arr, random_ordering=False):
    """
    :description: quicksort, in place

    :time: O(n^2) worst case, O(nlogn) average case. The worst case time is O(n^2) because, in the worst case, the input comes in sorted in reverse order or sorted order. If you take the end element as the pivot always, you will then iterate, for the ith pivot, through n-i elements which is still O(n^2) (i.e., the first recursive call will always do nothing, the second will sort n-i elements, giving a recurrence of T(n) = T(n-1) + Theta(n)). 

        BETTER: in expectation the algorithm will _not_ divide the array perfectly in half. Instead it will divide into some other fraction of left to right where that fraction isn't too bad. (what is this fraction? maybe? actually not sure maybe it is in half)

        WRONG: The average case is because each partition will in expectation divide the array in half, giving a recurrence of T(n) = 2T(n/2) + Theta(n), which is nlogn from master theorem. This is achieved in practice by swapping the pivot with a random element before sorting as in random_partition(...).

        Interestingly, so long as the split is a ratio rather than an absolute number of element reduction (e.g., T(n) = T(9/10 * n) + T(1/10 * n) + Theta(n)) the depth of the tree will still be Theta(logn), giving an overall runtime of Theta(nlogn).

        Intuitively, the gains made by quicksort are due to the fact that items partitioned into separate groups are never compared with each other.

    :space: O(1), done in place
    """

    def partition(arr, start, end):
        i = start - 1
        for j in range(i + 1, end):
            if arr[j] < arr[end]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
        arr[i], arr[end] = arr[end], arr[i]
        return i

    def random_partition(arr, start, end):
        idx = random.randint(start, end)
        arr[idx], arr[end] = arr[end], arr[idx]
        return partition(arr, start, end)

    
    def recurse(arr, start, end):
        if end > start:
            if random_ordering:
                pivot = random_partition(arr, start, end)
            else: 
                pivot = partition(arr, start, end)
            recurse(arr, start, pivot - 1)
            recurse(arr, pivot + 1, end)


    recurse(arr, 0, len(arr) - 1)
    return arr


if __name__ == '__main__':
    data = [[1,2,3],
            [1,3,4,6,8,67,5,43,2,2,34,6,6,6,74,3,2,3,4,4,54],
            [1],
            [4,3,2,1],
            [-4,-3,-5,-6, 5, 10]]

    overall = True
    for lst in data:
        sorted_data = tail_recursion_quicksort(copy.deepcopy(lst), random_ordering=False)
        print sorted_data
        result = sorted(lst) == sorted_data
        overall = overall and result
        print 'is the list sorted correctly?: {}'.format(result)
    print '\nwas everything correct?: {}'.format(overall)

"""
:additional notes: 
- what if everything has the same value? (7.2-2)
    - using the above method, this would result in a T(n) = T(n-1) + Theta(n) recurrence which would give O(n^2) runtime. This can be avoided by placing the pivot in the middle of congruent elements, but this would add a constant, which might or might not significantly hurt performance
- why is insertion sort better than quicksort of nearly ordered elements? (7.2-4)
    - the reason is because insertion sort maintains a sorted sublist that would only need to be partially searched to find the correct insertion location (and the search would involve few elements). Quicksort on the other hand would need to make recursive calls on nearly n - constant size lists giving it a runtime of O(n^2) 

"""

