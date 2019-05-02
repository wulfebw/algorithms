'''
The challenge here is to compute the medians in linear time 

you can do this using a modified counting sort 
by inserting and removing values from the counts 
to find the median in the new counts you have to figure out how the 
addition / subtraction of indices / values works
I think because it's the median you can have the running sum of the 
counts? and just 


oh ok
so there's two ways to do this
1. counting sort each time 
2. just do math to extract the median by looking at the sum
'''


import numpy as np

from counting_sort import counting_sort

def compute_medians(e,d, max_e=200):
    medians = [None] * (len(e) - d)
    for i in range(d, len(e)):
        medians[i-d] = counting_sort(e[i-d:i], max_e)[d // 2]
    return medians

def find_median_from_counts(c, d):
    med = d // 2
    total = 0
    for i, v in enumerate(c):
        total += v
        if total > med:
            return i

def compute_medians_fast(e, d, max_e=200):
    n = len(e)
    c = [0] * max_e
    for v in e[:d]:
        c[v] += 1
    
    medians = [0] * (n - d)
    medians[0] = find_median_from_counts(c, d)

    for i in range(d + 1, n):
        prev = e[i-1]
        c[prev] -= 1
        cur = e[i]
        c[cur] += 1
        medians[i - d] = find_median_from_counts(c, d)

    return medians

def notify(e,d):
    medians = compute_medians(e,d)
    c = 0 
    for i in range(d, len(e)):
        if e[i] >= medians[i-d] * 2:
            c += 1
    return c 

if __name__ == '__main__':

    inputs = [
        ([1,2,3,4,5,6,100,100], 4)
    ]
    for i in inputs:
        print(notify(*i))


    x = np.random.randint(0, 200, size=50)
    expect = compute_medians(x.copy(), 4)
    actual = compute_medians_fast(x.copy(), 4)
    np.testing.assert_array_equal(expect, actual)