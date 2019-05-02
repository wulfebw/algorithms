
import numpy as np

import utils

def partition(a, s, e):
    '''
    move pivot to the end
    then track the next position to place a value smaller than pivot (i)
    iterate array pivoting 
    insert pivot in the appropriate spot
    '''
    p = np.random.randint(s, e+1)
    a[p], a[e] = a[e], a[p]
    piv = a[e]
    i = s - 1
    for j in range(s, e):
        if a[j] < piv:
            i += 1 
            a[i], a[j] = a[j], a[i]
    a[i+1], a[e] = a[e], a[i+1]
    return i+1

def qsh(a,s,e):
    if e > s:
        q = partition(a, s, e)
        qsh(a, s, q - 1)
        qsh(a, q + 1, e)
    return a

def quick_sort(a):
    '''
    analysis:
    Θ(nlgn) average case
    Θ(n^2) worst case
    - worst case is when the pivots are selected in a manner such that 
        the array pivots entirely around it onto one side so that 
        the number of levels of recursive calls is lopsided and linear
    '''
    return qsh(a, 0, len(a) - 1)

if __name__ == '__main__':
    utils.test_sorting_algorithm(quick_sort)