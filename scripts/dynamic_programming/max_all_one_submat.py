
import numpy as np

def max_all_one_sub(a):
    '''
    Each index into the value array indicates the maximum size attainable 
    at that index.
    The way this works is you iterate the array
    at each index, you know that if the value is 0 then the max possible is 0
    but if it's a 1, then the best case is that this index is filling out the 
    lower right cell of a square of ones
    but this only occurs if all the surrounding cells have an equal value 
    if that's not the case, then you are only completing a square for the smallest
    this property is a result of moving through the array from top left to 
    bottom right
    '''
    n, m = a.shape
    v = np.zeros((n+1, m+1))
    for i in range(n):
        for j in range(m):
            if a[i,j] == 0:
                v[i+1,j+1] = 0
            else:
                v[i+1,j+1] = 1 + min(v[i,j], v[i+1,j], v[i,j+1])
    return int(np.max(v))


if __name__ == '__main__':
    inputs = [
        [[1]],

        [[1,0],
         [1,0]],

        [[1,1],
         [1,1]],

        [[0,1,1],
         [0,1,1],
         [1,1,0]],

        [[0,1,1,0],
         [1,1,1,1],
         [0,1,1,1],
         [1,1,1,1]]

    ]
    inputs = [np.array(v) for v in inputs]
    expect = [
        1,
        1,
        2,
        2,
        3,
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(max_all_one_sub(i))
        print()
