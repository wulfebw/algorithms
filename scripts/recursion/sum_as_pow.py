
import numpy as np
np.set_printoptions(threshold=10000)

def sum_as_pow(x, n):
    '''
    dynamic programming answer, though whether dynamic programming is necessary
    I'm not entirely sure
    O(x * x^(1/n))
    I guess you could check all of the combinations? but that's clearly worse 
    so yeah, I think this is the answer
    '''
    m = int(np.ceil(x ** (1/n))) + 1
    v = np.zeros((x+1,m+1))
    v[0,:] = 1
    for i in range(x):
        for j in range(m):
            row_if_used = i + 1 - j ** n
            if row_if_used >= 0:
                v[i+1,j+1] = v[i+1,j] + v[row_if_used,j]
            else:
                v[i+1,j+1] = v[i+1,j]
    return int(v[-1,-1])

if __name__ == '__main__':
    inputs = [
        (10 ,2),
        (100, 2)
    ]
    expect = [
        1,
        3
    ]
    for i,e in zip(inputs, expect):
        print(e)
        print(sum_as_pow(*i))
        print()