
import numpy as np

def max_cost_path_iterative(a):
    n,m = a.shape
    v = np.zeros((n+1,m+1))
    for i in range(n):
        for j in range(m):
            if i == 0: # first row, can only come from left
                maxcost = v[i+1,j]
            elif j == 0: # first col, can only come from above
                maxcost = v[i, j+1]
            else:
                maxcost = max(v[i+1,j], v[i,j+1])
            v[i+1,j+1] = a[i,j] + maxcost 
    n_steps = n + m - 1
    v_opt = (v / n_steps)[-1,-1]
    return v_opt

if __name__ == '__main__':
    inputs = [
        [[1,2,3],
         [4,5,6],
         [7,8,9]],

        [[1,4,3,2],
         [5,6,7,4],
         [9,6,1,1],
         [1,1,5,6]]
    ]
    inputs = [np.array(a) for a in inputs]
    expect = [
        (1+4+7+8+9) / 5.,
        (1+5+9+6+1+5+6) / 7.
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(max_cost_path_iterative(i))
        print()