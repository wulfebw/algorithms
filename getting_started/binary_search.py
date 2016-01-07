"""
:keywords: search, binary search
"""

def binary_search(lst, val):
    """
    :description: binary search for a value

    :time: O(nlogn)
    :space: O(1)
    """

    def recurse(lst, val, start, stop):
        if len(lst[start:stop]) <= 0:
            return -1

        cut = (stop - start) / 2 + start
        if lst[cut] == val:
            return cut
        elif lst[cut] > val:
            return recurse(lst, val, start, cut)
        else:
            return recurse(lst, val, cut + 1, stop)

    index = recurse(lst, val, 0, len(lst))
    return index

if __name__ == '__main__':
    data = [[1,2,3],
            [1,2,3,4,5,6,7],
            [-5,-4,-3,-2,-1,0,1,2,3,4,5],
            [1],
            [1, 1000],
            [1, 1000, 1000000]]
    vals = [3,4,-2,0,1000,1000]
    overall = True
    for lst, val in zip(data, vals):
        index = binary_search(lst, val)
        if index >= 0:
            print 'found at index: {}'.format(index)
        else:
            print 'value not in list'
        pyidx = lst.index(val) if val in lst else -1
        result = index == pyidx
        overall = overall and result
        print 'was the value found correctly?: {}'.format(result)
    print '\nall tests correct?: {}'.format(overall)

"""
:additional notes:
"""