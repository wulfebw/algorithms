
import collections

def decrement(d, v):
    d[v] -= 1
    if d[v] <= 0:
        del d[v]

def count_distinct_window(a, k):
    n = len(a)
    ctr = collections.defaultdict(int)
    for v in a[:k]:
        ctr[v] += 1
    distinct = []
    for (i,j) in zip(range(n), range(k, n)):
        distinct += [len(ctr)]
        decrement(ctr, a[i])
        ctr[a[j]] += 1
    distinct += [len(ctr)]
    return distinct

if __name__ == '__main__':

    inputs = [
        ([1,2,1,3,5], 3)
    ]
    for i in inputs:
        print(count_distinct_window(*i))