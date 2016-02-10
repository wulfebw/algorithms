
import copy

import heap_operations as heap_ops

def heapsort(arr):
    """
    :description: heapsort, version not in place b/c the heap ops don't take heap size parameter. Works by removing largest element and calling max_heapify

    :time: O(nlgn) worst case calls max_heapify n times

    :space: O(n)
    """
    heap = arr
    heap_ops.build_max_heap(heap)
    sorted_arr = []
    for i in range(len(arr) - 1):
        heap[0], heap[-1] = heap[-1], heap[0]
        sorted_arr.append(heap.pop())
        heap_ops.max_heapify(heap, 0)
    sorted_arr.append(heap.pop())
    return list(reversed(sorted_arr))

if __name__ == '__main__':
    data = [[1,2,3],
            [1,3,4,6,8,67,5,43,2,2,34,6,6,6,74,3,2,3,4,4,54],
            [1],
            [4,3,2,1],
            [-4,-3,-5,-6, 5, 10]]

    overall = True
    for lst in data:
        sorted_data = heapsort(copy.deepcopy(lst))
        result = sorted(lst) == sorted_data
        overall = overall and result
        print 'is the list sorted correctly?: {}'.format(result)
        if not result:
            print sorted_data
    print '\nwas everything correct?: {}'.format(overall)