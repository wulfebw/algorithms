
import collections
import copy

def valid_counts(c, sc):
    c = copy.deepcopy(c)
    sc = copy.deepcopy(sc)

    n = len(c.keys())
    total = sum(c.values())
    each = total // n

    free = 0
    for k,v in c.items():
        diff = v - each 
        if diff > 0:
            if sc[k] < diff:
                return False
            else:
                c[k] -= diff
                sc[k] -= diff
                free += sc[k]

    for k,v in c.items():
        diff = each - v
        if diff > 0:
            if free < diff:
                return False
            else:
                free -= diff
                c[k] += diff

    return True

def min_substring_equillibrium(a):
    n = len(a)
    c = collections.Counter(a)

    s = 0 
    e = 0
    minlen = n + 1
    sc = collections.Counter()

    while s < n:

        while not valid_counts(c, sc) and e < n:
            print('e ', e)
            input()
            e += 1
            sc[a[e-1]] += 1

        while valid_counts(c, sc) and s < n:
            print('s ', s)
            input()
            minlen = min(minlen, e - s)
            sc[a[s]] -= 1
            s += 1

        s += 1

    return minlen

if __name__ == '__main__':

    inputs = [
        'GAAATAAA'
    ]
    expected = [
        5
    ]

    for (i,e) in zip(inputs, expected):
        actual = min_substring_equillibrium(i)
        print('expected: {} actual: {}'.format(e, actual))
