"""
:keywords: sorting, selection sort
"""

import copy

def selection_sort(lst):
    """
    :description: inplace selection sort 

    :time: O(n^2)
    :space: O(1)
    """
    if len(lst) <= 1:
        return lst

    smallest_val = lst[0]
    smallest_idx = 0
    for insert_idx, val_at_insert in enumerate(lst):
        for cur_idx, cur_val in enumerate(lst[insert_idx:], insert_idx):
            if cur_val < smallest_val:
                smallest_val = cur_val
                smallest_idx = cur_idx
        lst[insert_idx], lst[smallest_idx] = smallest_val, val_at_insert
        smallest_val = lst[-1]
        smallest_idx = len(lst) - 1
    return lst


if __name__ == '__main__':
    data = [[1,2,3],
            [1,3,4,6,8,67,5,43,2,2,34,6,6,6,74,3,2,3,4,4,54],
            [1],
            [4,3,2,1],
            [-4,-3,-5,-6, 5, 10]]

    overall = True
    for lst in data:
        sorted_data = selection_sort(copy.deepcopy(lst))
        print sorted_data
        result = sorted(lst) == sorted_data
        overall = overall and result
        print 'is the list sorted correctly?: {}'.format(result)
    print '\nwas everything correct?: {}'.format(overall)