"""
:keywords: search
"""

def linear_search(lst, val):
    """
    :description: linear searching algorithm 

    :time: O(n) - goes through each element once
    :space: O(n) - space for the list
    """
    for idx, ele in enumerate(lst):
        if ele == val:
            return idx
    return -1

if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,88,9,9,6,65,3,4,3]
    val = 65
    index = linear_search(data, val)
    if index >= 0:
        print 'found at index: {}'.format(index)
    else:
        print 'value not in list'
    print 'was the value found correctly?: {}'.format(index == data.index(val))