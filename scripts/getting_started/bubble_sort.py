"""
:keywords: bubble sort, sorting
"""

import copy

def bubble_sort(lst):
    """
    :description: bubble sort - compare adjacent items n times, moving smaller to towards the front

    :time: O(n^2)
    :space: O(1)
    """
    if len(lst) < 2:
        return lst

    for i in range(len(lst)):
        for j in reversed(range(i + 1, len(lst))):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst

def bubble_sort_forward(lst):
    if len(lst) < 2:
        return lst

    for offset, _ in enumerate(lst):
        for base, _ in enumerate(lst[:-offset]):
            if lst[base] > lst[base + 1]:
                lst[base], lst[base + 1] = lst[base + 1], lst[base]

    return lst


if __name__ =='__main__':
    data = [[1,2,3],
            [1,3,4,6,8,67,5,43,2,2,34,6,6,6,74,3,2,3,4,4,54],
            [1],
            [4,3,2,1],
            [-4,-3,-5,-6, 5, 10],
            [1,2,3,3,2,1,1,2,3,3,2,1,1,1,1,3,2,1]]

    overall = True
    for lst in data:
        sorted_data = bubble_sort_forward(copy.deepcopy(lst))
        print sorted_data
        result = sorted(lst) == sorted_data
        overall = overall and result
        print 'is the list sorted correctly?: {}'.format(result)
    print '\nwas everything correct?: {}'.format(overall)

"""
:additional notes: 
- the indexing is a bit odd in this problem
    - not sure why to go forward vs backward
    - takeaway is that if you want to iterate through all pairs of elements multiple times that you can use the outer loop to dictate the number of times and the inner loop to perform the indexing of the pairs
- proving bubble sort correct
    1. init - at first you can say nothing about the list
    2. maintenance - after the first iteration of the inner loop you guarantee that the smallest element in the list will be in the first position. (prove this by definition: each two elements are compared. The smaller is moved left. The loop goes through each pair. Therefore the smallest must end on the left)
    3. termination - from (2) we know that when the ith outer loop finishes, up to the ith element will be in sorted order. Therefore, executing the outer loop length of array times gaurantees that the entire array will be sorted.
"""