"""
:keywords: binary, addition
"""

def add_binary(val1, val2):
    """
    :description: add two binary numbers represented as lists

    :time: ~O(5n)
    :space: O(n) since we make a new list
    """
    result =  [0] * (len(val1) + 1)
    carry = 0
    for idx, (v1, v2) in enumerate(zip(reversed(val1), reversed(val2))):
        total = v1 + v2 + carry
        cur = total % 2
        carry = 1 if total >= 2 else 0
        result[idx] = cur
    return list(reversed(result))

if __name__ == '__main__':
    val1 = [1,0,1,0,1]
    val2 = [0,0,1,0,1]
    summation = add_binary(val1, val2)
    print 'sum:\t',
    print summation
    print 'correctly added values?: {}'.format(summation == [0,1,1,0,1,0])
