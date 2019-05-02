
import numpy as np

def counting_sort(a, k):
    '''
    assume all the values are ints < k and also > 0 
    then you can just bucket them into their values
    and reproduce the counts 
    this is like a special case of bucket sort I think
    '''
    c = np.zeros(k, dtype=int)
    for v in a:
        c[v] += 1
    b = np.zeros(len(a), dtype=int)
    i = 0
    for j, v in enumerate(c):
        b[i:i+v] = j
        i += v
    return b 

if __name__ == '__main__':
    inputs = [
        ([1,2,4,5,6,7,6,4,3,3,2,1,2,3,4,5,8,9,2,2,2,3,4,4], 10),
    ]
    for i in inputs:
        print(np.array(sorted(i[0])))
        print(counting_sort(*i))