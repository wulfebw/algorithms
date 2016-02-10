
import sys

import heap_operations as heap_ops

def heap_max(heap):
    """
    :description: return the max element of the heap

    :time: O(1)
    """
    return heap[0]

def heap_extract_max(heap):
    """
    :description: remove and return the max value while maintaining the max heap property

    :time: O(lgn)
    """
    assert len(heap) > 0

    heap[0], heap[-1] = heap[-1], heap[0]
    max_value = heap.pop()
    heap_ops.max_heapify(heap, 0)
    return max_value

def heap_increase_key(heap, i, new_value):
    """
    :description: increase the value of a key and subsequently ensure max heap property is maintained

    :time: O(lgn) because moving the element with the new value to the top of the tree requires at most lgn operations
    """
    assert new_value > heap[i]

    heap[i] = new_value
    while heap[i] > heap[heap_ops.parent(i)]:
        heap[i], heap[heap_ops.parent(i)] = heap[heap_ops.parent(i)], heap[i]
        i = heap_ops.parent(i)

def heap_delete(heap, i):
    """
    :description: deletes an element from a max heap by changing its value to the max in the heap + 1 and then extracting the max value
    """
    heap_increase_key(heap, i, heap_max(heap) + 1)
    heap_extract_max(heap)

def max_heap_insert(heap, value):
    """
    :description: insert an element into the heap 

    :time: O(lgn)
    """
    heap.append(-sys.maxint)
    heap_increase_key(heap, len(heap) - 1, value)

if __name__ =='__main__':
    data = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,5,4,3,2,1,2,3,4,5]
    heap_ops.build_max_heap(data)
    result = heap_max(data) == max(data)
    print 'correct?: {}'.format(result)

    data = [1,2,3]
    heap_ops.build_max_heap(data)
    max_value = heap_extract_max(data)
    result = max_value == 3
    print 'correct?: {}'.format(result)
    result = data == [2,1]
    print 'correct?: {}'.format(result)

    data = [1,2,3]
    heap_ops.build_max_heap(data)
    heap_increase_key(data, 2, 10)
    result = data == [10, 2, 3] or data == [10, 3, 2]
    print 'correct?: {}'.format(result)

    data = [1,2,3]
    heap_ops.build_max_heap(data)
    max_heap_insert(data, 10)
    result = data == [10, 2, 3, 1] or data == [10, 3, 2, 1] or data == [10, 3, 1, 2]
    print 'correct?: {}'.format(result)

    data = [1,2,3]
    heap_ops.build_max_heap(data)
    heap_delete(data, 0)
    result = data == [2, 1]
    print 'correct?: {}'.format(result)
    data = [1,2,3]
    heap_ops.build_max_heap(data)
    heap_delete(data, 1)
    result = data == [3, 1]
    print 'correct?: {}'.format(result)
    data = [1,2,3]
    heap_ops.build_max_heap(data)
    heap_delete(data, 2)
    result = data == [3, 2]
    print 'correct?: {}'.format(result)



"""
:additional notes: 
6.5: Argue the correctness of HEAP-INCREASE-KEY
Initialization: prior to the first loop iteration the loop invariant must hold. This is because we swapped A[i] with a value strictly greater than it, making the new value larger than the children of A[i]. It may now be larger than its parent, however, giving us the single violation.
Maintenance: there are two options for what will occur once the loop begins executing:
A[i] < A[parent(i)]: this is the termination condition considered in part (iii)
A[i] > A[parent(i)]: in this case the loop executes in its entirety, swapping A[i] and A[parent(i)].
since A[i] > A[parent(i)], A[i] must be larger than or equal to the other child of A[parent(i)], so the loop invariant is not violated in this manner
since A[parent(i)] is larger than the original value of A[i] (as asserted prior to the call to the function), it must also be larger than the children of the original A[i] node, so the loop is not violated in this manner.
The only possible violation of the loop invariant at this point is the A[i] > A[parent(parent(i))], in which case, the loop invariant is strictly maintained
Termination: The loop stops executing for two reasons
A[i] has been swapped with its parent node until it becomes the root. Prior to this there could only have been one violation of the max heap property as asserted in (ii). After swapping with the root, we know that A[i] is the largest element (since it was swapped with the root) and therefore greater than or equal to the other child of the root. The original root was larger than the children of A[i] prior to the final swap, since it started out as such, so after the swap this property holds. Therefore on this termination criteria, the max heap property is maintained
A[i] is less than or equal to its new parent and the loop exits. In this case, the only possible violation of the max heap property (that A[i] > A[parent(i)]) was actually not a violation, therefore there are not violations and the max heap property holds.

"""




