'''
why not dynamic programming?
- because no repeated problems?
- because no overlapping problems?
'''

def recursive_power_sum_deprecated(x, n):
    '''
    doesn't work see below
    '''
    seen = set()
    maxval = int(x ** (1 / n))

    def recurse(x, minval, s):
        print(x)
        print(s)
        input()
        if x < 0:
            return 0
        elif x == 0:
            if s in seen:
                return 0
            else:
                seen.add(s)
                return 1
        else:
            count = 0
            for v in range(minval, maxval + 1):
                count += recurse(x - v ** n, minval + 1, s + (v,))
            return count

    count = recurse(x, 1, tuple())
    return count

def recursive_power_sum(x, n):
    
    def recurse(x, v):
        if x < 0:
            return 0
        elif x == 0:
            return 1
        elif v == 0:
            return 0
        else:
            include = recurse(x - v ** n, v - 1)
            exclude = recurse(x, v - 1)
            return include + exclude

    maxval = int(x ** (1 / n))
    return recurse(x, maxval)

if __name__ == '__main__':

    inputs = [
        (10,2),
        (100,2),
        (100,3)
    ]
    expected = [
        1,
        3,
        1
    ]
    fn = recursive_power_sum

    for (i,e) in zip(inputs, expected):
        actual = fn(*i)
        print('expected: {}\tactual: {}'.format(e, actual))