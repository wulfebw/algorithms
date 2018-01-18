'''
A note on which previous cells you have to check 
in the below case, you just have to check the cells directly next to the 
current cell 
the reason is that the other checks will already be performed by the nearby 
cells 
The unneeded cells are commneted out
'''
import numpy as np

def lcs_3(a, b, c):
    n,m,l = len(a), len(b), len(c)
    v = np.zeros((n+1,m+1,l+1))
    for i in range(n):
        for j in range(m):
            for k in range(l):
                if a[i] == b[j] == c[k]:
                    v[i+1,j+1,k+1] = v[i,j,k] + 1
                else:
                    v[i+1,j+1,k+1] = max(
                        # v[i,j,k],
                        # v[i+1,j,k],
                        # v[i,j+1,k],
                        # v[i,j,k+1],
                        v[i+1,j+1,k],
                        v[i+1,j,k+1],
                        v[i,j+1,k+1]
                    )
    return int(v[-1,-1,-1])

if __name__ == '__main__':
    inputs = [
        ('aaaabbb','aabbb','aa'),
        ('abcd1e2', 'bc12ea', 'bd1ea'),
        ('asdfasdfhd', 'askdjfh', 'asdfkjha')
    ]

    expect = [
        2,
        3,
        5
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(lcs_3(*i))
        print()