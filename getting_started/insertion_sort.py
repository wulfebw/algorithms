"""
:keywords: sorting, insertion sort
"""

import copy

def insertion_sort(lst):
    """
    :description: inplace insertion sort. Main ideas:
            1. concept of loop invariance - specficially that lst[0...comparison_index] is always sorted
            2. inplace here simply means moving values from one index to another rather than using a separate array

    :time: O(n^2) - two loops in worst case in reverse order requires n * n comparisons
    :space: O(n) - one temporary variable holds a value plus the size of the array

                                                                            # cost      # times
    for i in range(1, len(lst)):                                            # c1        # n
        cur = lst[i]                                                        # c2        # n - 1
        comparison_index = i - 1                                            # c3        # n - 1
        while comparison_index >= 0 and lst[comparison_index] > cur:        # c4        # n - 1
            lst[comparison_index + 1] = lst[comparison_index]               # c5        # SUM 1 to n (t)
            comparison_index -= 1                                           # c6        # SUM 1 to n (t)
        lst[comparison_index + 1] = cur                                     # c7        # n - 1
    return lst                                                              # c8        # 1

    - to get the time complexity, sum the product of cost and times over all the lines
    - with this representation it is easy to evaluate the best, average, and worst case runtimes
    - here we consider the largest term in the expression: c5 * SUM 1 to n (t)
    - which equals c5 * n(n-1) / 2 operations
    - therefore O(n^2)

    """
    for i in range(1, len(lst)):
        cur = lst[i]
        comparison_index = i - 1
        while comparison_index >= 0 and lst[comparison_index] > cur:
            lst[comparison_index + 1] = lst[comparison_index]
            comparison_index -= 1
        lst[comparison_index + 1] = cur
    return lst

if __name__ == '__main__':
    data = [1,3,4,6,8,67,5,43,2,2,34,6,6,6,74,3,2,3,4,4,54]
    sorted_data = insertion_sort(copy.deepcopy(data))
    print sorted_data
    print 'is the list sorted correctly?: {}'.format(sorted(data) == sorted_data)

"""
:additional notes:
    - how do we show this is correct?
        - show loop invariant property holds. Do this through three assertions
            1. initialization = property is true before the looping
            2. maintenance = property remains true through a loop if it starts true
            3. termination = when loop terminates we have a claim that the property is still true
    - this is a general method of showing that an algorithm works
    - call it loop invariance
    - so for the case of insertion sort
        0. the property we want to maintain is that everything in the list before the current element is already sorted i.e., lst[1...j-1] is sorted
        1. initialization - at first there is one element so it is sorted
        2. maintenance - we compare the current element to those prior to it in the list
            - base case: if we reach the front of the list we stop
            - if the current element is larger we stop
            - if it is smaller we keep going, moving the larger element forward in the list therefore maintaining this property
            - we insert the current element when we find a point where [j-1] < [j] < [j+1]
        3. termination - since this property held before looping and during looping, we can believe that it holds after looping
    - essentially proof by induction
"""