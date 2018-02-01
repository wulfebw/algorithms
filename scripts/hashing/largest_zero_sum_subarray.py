

def naive_largest_zero_sum_subarray(a):
    best = 0
    for i in range(len(a)):
        total = a[i]
        for j in range(i+1, len(a)):
            total += a[j]
            if total == 0:
                best = max(best, j - i + 1)
    return best

def largest_zero_sum_subarray(a):
    '''
    the way this works is by recognizing when the total goes from a value 
    to that same value again
    whenever this occurs, the intervening array entries must sum to zero
    '''
    sums = dict()
    maxlen = 0
    total = 0
    for i in range(len(a)):
        total += a[i]
        
        if a[i] == 0 and maxlen == 0:
            maxlen = 1
        if total == 0:
            maxlen = i + 1
        if total in sums.keys():
            maxlen = max(maxlen, i - sums[total])
        else:
            # only add the sum if haven't seen before
            sums[total] = i

    return maxlen

if __name__ == '__main__':

    inputs = [
        [15,-2,2,-8,1,7,10,23],
        [0,0,0,0,0,0,0,0],
        [1,-1,1,-1,1],
        [-15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    expect = [
        5,
        8,
        4,
        16
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(naive_largest_zero_sum_subarray(i))
        print(largest_zero_sum_subarray(i))
        print()
