
import numpy as np

def compute_max_value(jobs):
    h = max([t[1] for t in jobs])
    m = len(jobs)
    v = np.zeros((h+1, m+1))
    for i in range(h):
        for j in range(m):
            s,f,p = jobs[j]
            # if the job finishes at this pt in time
            # i+1 b/c f is 1 based
            if i+1 == f: 
                v[i+1,j+1] = max(
                    v[i+1,j],
                    # we would move to s (not s+1 b/c 1-based indexing is used)
                    v[s,j] + p
                )
            else:
                v[i+1,j+1] = v[i+1,j]
    return int(v[-1,-1])

if __name__ == '__main__':
    inputs = [
        [
            (1,2,50),
            (3,5,20),
            (6,19,100),
            (2,100,200)
        ],
        [
            (1,2,10),
            (2,4,10),
            (4,6,10),
            (2,5,0),
            (5,10,100)
        ]
    ]
    expect = [
        250,
        110
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(compute_max_value(i))
        print()
