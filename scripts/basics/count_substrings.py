
import numpy as np 


def count_substrings(a):
    cnt = 0
    n = len(a)
    for i in range(n-1):
        if a[i] == 1:
            for j in range(i+1,n):
                if a[j] == 1:
                    cnt += 1 
    return cnt

def count_substrings_cumsum(a):
    s = list(reversed(np.cumsum(list(reversed(a)))))
    cnt = 0 
    n = len(a)
    for i in range(n-1):
        if a[i] == 1:
            cnt += s[i+1]
    return cnt

def count_substrings_eq(a):
    c = sum(a)
    # total pairs of substrings
    return c * (c - 1) / 2


if __name__ =='__main__':
    inputs = [
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,1,0,1],
        [1,1,1,1],
        [int(v) for v in '100100000111111101010010010011010101110110']
    ]
    expect = [
        6,
        3,
        6,
        231
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(count_substrings(i))
        print(count_substrings_cumsum(i))
        print(count_substrings_eq(i))
        print()

