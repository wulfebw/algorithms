
import numpy as np

def compute_optimal_value(w, p, c):
    m = len(w)
    v = np.zeros((c+1, m+1))
    for i in range(c):
        for j in range(m):
            if i+1 - w[j] >= 0: # capacity >= weight
                v[i+1,j+1] = max(
                    v[i+1,j], # don't add the item
                    v[i+1 - w[j], j] + p[j] # do add the item
                )
            else:
                v[i+1,j+1] = v[i+1,j] # cannot fit item, skip it
    # does the optimal solution always end up in the bottom right?
    # I guess it does because it's the max across the row
    # and each item in the row is max across the column
    return int(v[-1,-1])

if __name__ == '__main__':
    inputs = [
        ([10,20,30], [60,100,120], 50)
    ]
    expect = [
        220
    ]
    for (i, e) in zip(inputs, expect):
        print(e)
        print(compute_optimal_value(*i))
        print()
