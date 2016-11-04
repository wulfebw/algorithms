
import copy
import collections
import heapq
import numpy as np
import time 

def generate_data(num_samples=10000, num_arr=100):
    assert num_samples % num_arr == 0
    data = np.random.randn(num_samples)
    return [collections.deque(sorted(values))
        for values in data.reshape(num_arr, -1)]

def sort_k_sorted_lists_min_heap(data):
    """
    data shape = (num_arr, num_samples_each)

    time complexity: m = num_arr, k = num_samples_each
    m to load into heap
    heappop O(1)
    heappush O(logm)
    so the question is how many times do you push?
    once for each element so O(m*k*logm)
    """
    sorted_data = []
    heap = []

    for idx, arr in enumerate(data):
        heapq.heappush(heap, (arr.popleft(), idx))

    while len(heap) > 0:
        value, arr_idx = heapq.heappop(heap)
        sorted_data.append(value)
        if len(data[arr_idx]) > 0:
            heapq.heappush(heap, (data[arr_idx].popleft(), arr_idx))

    return sorted_data

def merge(arr_1, arr_2):
    merged = collections.deque()
    while len(arr_1) > 0 and len(arr_2) > 0:
        if arr_1[0] < arr_2[0]:
            merged.append(arr_1.popleft())
        else:
            merged.append(arr_2.popleft())

    if arr_1:
        merged.extend(arr_1)
    else:
        merged.extend(arr_2)

    return merged

def sort_k_sorted_lists_merge_sort(data):
    """
    time complexity: m = num_arr, k = num_samples_each
    log(m) depth of calls to recurse
    each level in that depth performs m*k operations
    so in total it should be O(m*klogm)
    """

    def recurse(data):
        length = len(data)

        if length == 1:
            return data[0]

        if length == 2:
            return merge(data[0], data[1])

        med = length / 2
        lower = data[:med]
        upper = data[med:]

        return merge(recurse(lower), recurse(upper))

    return recurse(data)

def time_function(f, gen, num_runs=100):
    st = time.time()
    for run in range(num_runs):
        f(gen())
    et = time.time()
    return et - st

if __name__ == '__main__':
    data = generate_data(1000, 1000)
    expected_sorted_data = sorted(np.reshape(data, (-1)))

    # min heap method
    # actual_sorted_data = sort_k_sorted_lists_min_heap(data)
    # assert actual_sorted_data == expected_sorted_data

    # merge method
    # actual_sorted_data = sort_k_sorted_lists_merge_sort(data)
    # assert expected_sorted_data == list(actual_sorted_data)

    # time them 
    heap_time = time_function(sort_k_sorted_lists_min_heap, generate_data)
    merge_time = time_function(sort_k_sorted_lists_merge_sort, generate_data)
    print('heap: {:.5f} sec\tmerge: {:.5f} sec'.format(heap_time, merge_time))
