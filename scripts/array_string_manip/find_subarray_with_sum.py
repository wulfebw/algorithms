
def find_subarray_with_sum_naive(a, k):
    n = len(a)
    for i in range(n):
        total = a[i]
        if total == k:
            return i,i
        for j in range(i + 1, n):
            total += a[j]
            if total == k:
                return i,j
    return -1,-1

def find_subarray_with_sum(a, k):
    # edge cases of len 0 or 1 arrays
    if len(a) == 0:
        return -1, -1
    elif len(a) == 1:
        return (0,0) if a[0] == k else (-1,-1)

    n = len(a)
    i = 0 # next to remove
    j = 1 # next to add
    total = a[0]

    while j < n:

        if total == k:
            return i, j - 1
        elif total < k:
            total += a[j]
            j += 1
        else: # total > k
            total -= a[i]
            i += 1

            if i == j:
                total += a[j]
                j += 1

    # adding last element might have hit total, check for that
    if total == k:
        return i, j - 1
    return -1, -1

if __name__ == '__main__':

    inputs = [
        ([1,4,20,3,10,5], 33),
        ([1,4,0,0,3,10,5], 7),
        ([1,4], 0),
        ([15, 2, 4, 8, 9, 5, 10, 23], 23)
    ]

    for i in inputs:
        print(find_subarray_with_sum(*i))

