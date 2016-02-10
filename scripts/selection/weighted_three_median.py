"""
:question: what is a weighted median? Does the original order of the data matter at all?
"""

from median import randomized_select as select

def weighted_three_median_via_sort(arr):
    """
    :description: returns the weighted three median by sorting the array and traversing it. Returns the value and the original index

    :time: O(nlgn)
    """
    if len(arr) < 1:
        raise ValueError
    if len(arr) == 1:
        return arr[0]

    values_with_indicies = [(val, idx) for idx, val in enumerate(arr)]
    sorted_values = sorted(values_with_indicies)

    upper_sum = sum(arr)
    lower_bound = (1. / 3) * upper_sum
    upper_bound = (2. / 3) * upper_sum
    lower_sum = 0
    
    for idx, (val, orig_idx) in enumerate(sorted_values):
        upper_sum -= val
        if lower_sum <= lower_bound and upper_sum <= upper_bound:
            return val, orig_idx
        lower_sum += val

def weighted_three_median_via_select(arr):
    """
    :description: returns the weighted three median through use of select. Returns just the value.

    :time: O(n) because the recurrence is T(n) = T(n/2) + O(n), which is O(n)
    """

    lower_bound = (1. / 3) * sum(arr)
    upper_bound = (2. / 3) * sum(arr)

    def recurse(arr, start, end, before_start_sum, after_end_sum):
        # partition array, and retrieve current medians index in array
        order_statistic = (end - start) / 2
        median_value, pivot_idx = select(arr, order_statistic)

        # collect current sums
        cur_lower_sum = sum(arr[start: pivot_idx])
        cur_upper_sum = sum(arr[pivot_idx + 1: end])

        # bounds satisfied by current median
        if before_start_sum + cur_lower_sum <= lower_bound and after_end_sum + cur_upper_sum <= upper_bound:
            return median_value
            
        # recurse on current lower half
        elif before_start_sum + cur_lower_sum > lower_bound:
            new_after_end_sum = after_end_sum + cur_upper_sum + median_value
            new_end = pivot_idx
            return recurse(arr, start, new_end, before_start_sum, new_after_end_sum)

        # recurse on current upper half
        else:
            new_before_start_sum = before_start_sum + cur_lower_sum + median_value
            new_start = pivot_idx + 1
            return recurse(arr, new_start, end, new_before_start_sum, after_end_sum)

    return recurse(arr, 0, len(arr), 0, 0)

if __name__ == '__main__':
    data = [[4,3,2,1],
            [10,7,3,1],
            [3,4,5],
            [10,11],
            [0.0001, 10,11],
            [2,1]]
    # format: (value of 3-median, idx of 3-median)
    expecteds_sort = [(3, 1), (7,1), (4,1), (10,0), (10,1), (1,1)]
    
    func = weighted_three_median_via_select
    if func == weighted_three_median_via_select:
        expecteds = [3, 7, 4, 10, 10, 2]
    else:
        expecteds = [(3, 1), (7,1), (4,1), (10,0), (10,1), (1,1)]

    overall = True
    result = True
    for arr, expected in zip(data, expecteds):
        actual = func(arr)
        result = actual == expected
        if result:
            print 'correct'
        else: 
            print 'incorrect result for arr: {}'.format(arr)
            print 'expected: {}\tactual: {}\n'.format(expected, actual)
        overall = overall and result

    print 'everything correct?: {}'.format(overall)