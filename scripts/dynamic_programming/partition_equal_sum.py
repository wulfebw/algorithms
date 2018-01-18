'''
Idea is that for there to be a partition, then one of these subsets must 
add up to half the sum
so with that you just have a "do these add up" problem, which is a known DP problem
and part of the include / exclude category
'''
import numpy as np 

def partition(a):
    if sum(a) % 2 != 0:
        return False
    s = sum(a) // 2
    m = len(a)
    v = np.zeros((s+1,m+1))
    v[0,:] = 1
    for i in range(s):
        for j in range(m):
            if i+1 - a[j] >= 0:
                v[i+1,j+1] = max(
                    v[i+1,j],
                    v[i+1 - a[j],j]
                )
            else:
                v[i+1,j+1] = v[i+1,j]
    return v[-1,-1] == 1

if __name__ == '__main__':
    inputs = [
        [1,2,3,4,5,5],
        [2,3,4,5,5],
        [1,2],
        [1,2,3],
        [3,4,5,6,7,5],
        [100,1,50,25,25,2,1,1,1]
    ]
    expect = [
        True,
        False,
        False,
        True,
        True,
        True
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(partition(i))
        print()
