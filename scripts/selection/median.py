"""
:keywords: selection
"""

import numpy as np
import random
import time

def select(arr, i):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return arr[0]

def randomized_select(arr, i):
    """
    :description: select the ith smallest element from the array

    :time: O(n^2) worst case, but O(n) average case. The worst case comes from the fact that we could theoretically select the largest element to partion around each time, and additionally have the ith element be the last element checked. this would result in checking each element once for each pivot (of which there are n-1) giving O(n^2). The average case is due to the fact that on average, we break the array in about half, and only consider one of those halves. The proof that it is expected O(n) is actually pretty invovled it seems so I'm skipping it for now but see page 218 if you're interested.
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

    def recurse(arr, start, end, i):
        if start == end:
            return arr[start], start

        pivot = random_partition(arr, start, end)

        if pivot == i:
            return arr[pivot], pivot
        elif pivot < i:
            return recurse(arr, pivot + 1, end, i)
        else:
            return recurse(arr, start, pivot - 1, i)

    return recurse(arr, 0, len(arr) - 1, i)

def test_median_correctness(func=randomized_select):
    data = [[2,1,3],
            [1,2,3,4,5,6,7,8,9],
            [9,8,7,6,5,4,3,2,1],
            [-1,0,1],
            [5,6,4,7,3,8,2,9,1],
            [100,1001,10000,100000,1000000]
            ]
    expecteds = [2, 5, 5, 0, 5, 10000]
    overall = True
    for arr, expected in zip(data, expecteds):
        med_idx = len(arr) / 2
        if func == randomized_select:
            actual, idx = func(arr, med_idx)
        elif func == np.partition:
            actual = np.partition(arr, med_idx)[med_idx]
        result = actual == expected
        overall = result and overall
        if result:
            print 'correct'
        else:
            print 'incorrect for arr: {}, expected: {}, got: {}'.format(arr, expected, actual)
    print 'got everything right?: {}'.format(overall)

def test_order_statistic_correctness(func=randomized_select):
    data = [[2,1,3],
            [1,2,3,4,5,6,7,8,9],
            [9,8,7,6,5,4,3,2,1],
            [-1,0,1],
            [5,6,4,7,3,8,2,9,1],
            [100,1001,10000,100000,1000000]
            ]
    expecteds = [3, 3, 3, 1, 3, 10000]
    overall = True
    for arr, expected in zip(data, expecteds):
        stat_idx = 2
        if func == randomized_select:
            actual, idx = func(arr, stat_idx)
        elif func == np.partition:
            actual = np.partition(arr, stat_idx)[stat_idx]
        result = actual == expected
        overall = result and overall
        if result:
            print 'correct'
        else:
            print 'incorrect for arr: {}, expected: {}, got: {}'.format(arr, expected, actual)
    print 'got everything right?: {}'.format(overall)

def test_order_statistic_performance(func=randomized_select):
    num_runs = 100000
    num_samples = 2 ** 16
    k = num_samples / 2
    st = time.time()
    for run in range(num_runs):
        data = np.random.permutation(np.arange(num_samples))
        if func == randomized_select:
            med, idx = func(data, k)
        elif func == np.partition:
            med = func(data, k)[k]
    print 'func: {}\tmedian: {}\ttime: {}'.format(func, med, time.time() - st)

if __name__ == '__main__':
    test_order_statistic_correctness()
    test_order_statistic_correctness(np.partition)
    test_median_correctness()
    test_median_correctness(np.partition)
    # test_order_statistic_performance()
    test_order_statistic_performance(np.partition)
    