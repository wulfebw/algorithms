'''
I actually didn't get this problem right, but I don't think it's a great problem 
but would still be good practice
'''

import numpy as np

def max_prod_cutting_val(n):
    m = n - 1
    v = np.zeros((n+1, m+1))
    v[0,:] = 1
    for i in range(n):
        for j in range(m):
            if i >= j:
                v[i+1,j+1] = max(
                    v[i+1,j],
                    v[(i+1) - (j+1),j] * (j+1)
                )
            else:
                v[i+1,j+1] = v[i+1,j]
    return v[-1,-1]

if __name__ == '__main__':
    inputs = [
        2,
        3,
        4,5,10
    ]
    expect = [
        1,
        2,
        4,6,36
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(max_prod_cutting_val(i))
        print()