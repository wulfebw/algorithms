

def find_smallest_subarray_with_sum(a, k):

    if len(a) == 0:
        return 0 if k == 0 else -1

    n = len(a)
    total = 0
    s = 0
    e = 0
    minlength = n + 1

    while e < n:

        # add onto subarray from right while smaller
        while total <= k and e < n:
            total += a[e]
            e += 1

        # remove from left when larger
        while total > k and s < n:
            minlength = min(minlength, e - s)
            total -= a[s]
            s += 1

    if minlength > n:
        return -1
    else:
        return minlength

if __name__ == '__main__':

    inputs = [
        ([1, 4, 45, 6, 0, 19],51),
        ([1, 10, 5, 2, 7],9),
        ([1, 11, 100, 1, 0, 200, 3, 2, 1, 250],280),
        ([1,2,4],8),

    ]
    expect = [
        3,
        1,
        4,
        -1
    ]

    for (i,e) in zip(inputs, expect):
        print('actual: {}'.format(find_smallest_subarray_with_sum(*i)))
        print('expected: {}\n'.format(e))
