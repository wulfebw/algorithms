
import numpy as np
import time

def unique_bst(values):
    '''
    what's the time complexity of this?
    without caching, it's n * 2^n
    but with caching it's less clear 
    I think the possibilities are 
    O(n^2) with a terrible constant

    apparently it's a catalan number and you can just compute it 
    '''
    cache = {}
    values = list(sorted(values))

    def recurse(a):
        if len(a) <= 1:
            return 1
        elif tuple(a) in cache.keys():
            return cache[tuple(a)]
        else:
            total = 0
            for i in range(len(a)):
                nleft = recurse(a[:i])
                nright = recurse(a[i+1:])
                total += nleft * nright

            cache[tuple(a)] = total
            return total

    return recurse(values)


def unique_bst_iterative(a):
    n = len(a)
    v = np.ones(n+1)
    for i in range(1, n):
        total = 0
        for j in range(i+1):
            total += v[i-j] * v[j]
        v[i+1] = total
    return v[-1]

if __name__ == '__main__':
    # inputs = [
    #     [1,2],
    #     [1,2,3]
    # ]
    # expect = [
    #     2,
    #     5
    # ]
    # for (i,e) in zip(inputs, expect):
    #     print(e)
    #     print(unique_bst_iterative(i))
    #     print()
    times = []
    for i in range(2,1000):
        print(i)
        st = time.time()
        unique_bst_iterative(list(range(i)))
        times.append(time.time() - st)

    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    plt.plot(range(len(times)), times)
    plt.show()