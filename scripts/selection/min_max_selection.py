
import numpy as np

def maximum(lst):
    if lst is None or lst == []:
        return lst
    if len(lst) == 1:
        return lst[0]

    max_val = lst[0]
    for val in lst:
        if val > max_val:
            max_val = val
    return max_val

def minimum(lst):
    if lst is None or lst == []:
        return lst
    if len(lst) == 1:
        return lst[0]

    min_val = lst[0]
    for val in lst:
        if val < min_val:
            min_val = val
    return min_val

def max_min(lst):
    if lst is None or lst == []:
        return lst, lst
    if len(lst) == 1:
        return lst[0], lst[0]

    if lst[0] < lst[1]:
        min_val = lst[0]
        max_val = lst[1]
    else:
        min_val = lst[1]
        max_val = lst[0]

    for i in range(len(lst) - 1):
        first = lst[i]
        second = lst[i + 1]
        if first < second:
            if first < min_val:
                min_val = first
            if second > max_val:
                max_val = second
        else:
            if first > max_val:
                max_val = first
            if second < min_val:
                min_val = second
    return max_val, min_val


def run(lst):
    return maximum(lst), minimum(lst)
    # return max_min(lst)

if __name__ == '__main__':
    data = [[],
            [1],
            [1,2,3],
            [-1,-2,-3],
            [-1,-3,0,1,3],
            [1000, -1000, 1, -1],
            np.arange(100000)]
    overall = True
    for lst in data:
        expected_max = max(lst) if lst != [] else []
        expected_min = min(lst) if lst != [] else []
        actual_max, actual_min = run(lst)
        result = expected_max == actual_max and expected_min == actual_min
        print("for list: {}, max: {}, min: {}, correct?: {}".format(lst, actual_max, actual_min, result))
        overall = overall and result
    print("was everything correct?: {}".format(overall))

