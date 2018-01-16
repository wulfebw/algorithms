'''
this solution is O(n^2)
theres a solutions that O(nlgn)
but haven't implemented it here
'''

import numpy as np

import context_timer

def lis_recursive(a):
    cache = dict()

    def recurse(i):
        if i == 0: 
            return 0, -np.inf
        elif i in cache.keys(): 
            return cache[i]
        else:
            longest, maxval = 0, -np.inf
            aval = a[i-1]
            for j in range(i):
                cur, curval = recurse(j)
                if curval <= aval and cur + 1 > longest:
                    longest = cur + 1
                    maxval = aval
            cache[i] = (longest, maxval)
            return (longest, maxval)

    return recurse(len(a))[0]

def lis_iterative(a):
    '''
    Basically, if we know the solution to every subproblem before, then all we
    have to do is ask, "can we add this to any of those subproblem solutions? 
    and for all for which we can add it, what's the maximum resulting length?"
    '''
    v = np.ones(len(a))
    for i in range(len(a)):
        for j in range(i):
            if a[j] <= a[i]:
                v[i] = max(v[j]+1, v[i])
    return int(np.max(v))

if __name__ == '__main__':
    inputs = [
        [3, 10, 2, 1, 20],
        [3,2],
        [50, 3, 10, 7, 40, 80],
        [10, 22, 9, 33, 21, 50, 41, 60]
    ]
    expect = [
        3,
        1,
        4,
        5
    ]

    for (i,e) in zip(inputs, expect):
        print(e)
        with context_timer.ContextTimer():
            print(lis_recursive(i))
        with context_timer.ContextTimer():
            print(lis_iterative(i))
        print()