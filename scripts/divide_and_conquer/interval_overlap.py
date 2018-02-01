'''
given a sorted list of intervals (xi,yi)
find the pair of intervals with the largest overlap (max(xi,xj),min(yi,yi))
'''


def naive_max_overlap(a):
    '''
    compare each pair = choose(n,2) = O(n^2)
    '''
    maxoverlap = 0
    for i, r1 in enumerate(a):
        for r2 in a[i+1:]:
            maxoverlap = max(maxoverlap, min(r1[1], r2[1]) - r2[0])
    return maxoverlap

def max_overlap(a, s, e):
    '''
    merge sort style divide + O(n)
    therefore T(n) = 2T(n/2) + O(n) = O(nlgn)
    '''
    if s >= e:
        return 0

    mid = (s + e) // 2
    left = max_overlap(a, s, mid)
    right = max_overlap(a, mid+1, e)
    max_j = max([j[1] for j in a[s:mid+1]])
    cross = max([min(max_j, r[1]) - r[0] for r in a[mid+1:]])
    return max(left, right, cross)

if __name__ == '__main__':

    inputs = [
        [(1,3),(1,10),(5,7),(5,10)],
    ]
    expect = [
        5
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(naive_max_overlap(i))
        print(max_overlap(i, 0, len(i) - 1))
        print()