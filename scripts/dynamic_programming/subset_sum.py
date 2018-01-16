'''
This is one of those problems where the obvious recursive solution is in 
terms of the possible values that you can use, or rather, is a non linear 
function of the number of those values, whereas the iterative solution is 
a linear function of them

At least I thought that was the case, but when you run these, their runtime 
is about the same?
Ok, it's more nuanced
- the recursive solution runtime depends heavily on the problem, which is 
typically undesireable, and in the worst case might be exponential in m?
    + 
- the iterative solutions are 
'''

import numpy as np

from context_timer import ContextTimer

def subset_sum(n, vals):
    vals = list(sorted(vals))
    cache = dict()

    def recurse(n, vals):
        if n == 0:
            return True
        elif len(vals) == 0:
            return False
        elif (n, tuple(vals)) in cache.keys():
            return cache[(n, tuple(vals))]
        else:
            for i, v in enumerate(vals):
                vals_without = vals[:i] + vals[i+1:]
                able = recurse(n - v, vals_without)
                cache[(n-v, tuple(vals_without))] = able
                if able:
                    return True
            return False

    return recurse(n, vals)

def subset_sum_iterative(n, vals):
    '''
    The way this works is it says, for each possible sum you could encounter
    that sum is true (i.e., can be achieved) if either of two things is true
    1. that from that sum, you ignore one of the possible set values and continue on 
    2. that you subtract that set value and continue on
    so you're answering the question, do we _ever_ use this value in the set?
    it doesn't matter what order you do this in
    '''
    m = len(vals)
    v = np.zeros((n+1,m+1))
    v[0,:] = 1 # gets to first row, then it's possible
    for i in range(n):
        for j in range(m):
            if i+1 - vals[j] >= 0:
                v[i+1,j+1] = max(v[i+1-vals[j],j], v[i+1,j])
            else:
                v[i+1,j+1] = v[i+1,j]
    return v[-1,-1] == 1

def subset_sum_iterative_fast(st, n, sm) :
    '''
    didn't write this and I think it's wrong
    '''
   
    # The value of subset[i][j] will be
    # true if there is a subset of 
    # set[0..j-1] with sum equal to i
    subset=[[Trueß] * (sm+1)] * (n+1)
   
    # If sum is 0, then answer is true
    for i in range(0, n+1) :
        subset[i][0] = True
   
    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sm + 1) :
        subset[0][i] = False
   
    # Fill the subset table in botton 
    # up manner
    for i in range(1, n+1) :
        for j in range(1, sm+1) :
            if(j < st[i-1]) :
                subset[i][j] = subset[i-1][j]
            if (j >= st[i-1]) :
                subset[i][j] = subset[i-1][j] or subset[i - 1][j-st[i-1]]
   
   
    return subset[n][sm];

if __name__ == '__main__':

    inputs = [
        (9, [3, 34, 4, 12, 5, 2]),
        (6, [1,2,3]),
        (7, [1,2,3]),
        (100, [5,8,12,15,10,25,25,50]),
        (101, [5,8,12,15,10,25,25,50]),
        (100000, np.arange(15))
    ]
    expect = [
        True,
        True,
        False,
        True,
        False,
        False
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        with ContextTimer():
            print(subset_sum(*i))
        with ContextTimer():
            print(subset_sum_iterative(*i))
        with ContextTimer():
            print(subset_sum_iterative_fast(i[1],len(i[1]),i[0]))
        print()