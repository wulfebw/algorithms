
import numpy as np

def schedule(a, t, e, x):
    a, t = np.array(a), np.array(t)
    m = np.shape(a)[1]
    v = np.zeros((2,m+2))
    v[:,0] = e
    v[:,-1] = x
    for j in range(m):
        v[0,j+1] = min(v[0,j] + a[0,j], v[1,j] + a[1,j] + t[0,j])
        v[1,j+1] = min(v[1,j] + a[1,j], v[0,j] + a[0,j] + t[1,j])
    v[:,-1] += v[:,-2]
    print(v)
    return np.min(v[:,-1])

if __name__ == '__main__':
    inputs = [
        (
            [[4,5,3,2],[2,10,1,4]], 
            [[0,7,4,5],[0,9,2,8]], 
            [10,12], 
            [18,7]
        )
    ]
    expect = [
        35
    ]

    for (i,e) in zip(inputs, expect):
        print(e)
        print(schedule(*i))
        print()