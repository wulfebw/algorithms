
import numpy as np

def compute_prod_seq_term(n):
    '''
    O(n) ? or O(n^2) ?
    how many recursive calls are made? n 
    how much work per call? n 
    so O(n^2)
    the recurrence is T(n) = T(n-1) + O(n)
    which you can't apply the master theorem to 
    but you can just logic it out
    there are n levels to this tree 
    each time you do the current levels worth of work 
    but this turns out to be O(n) work at each level 
    so overall it's O(n^2)
    '''
    if n == 0:
        return 0
    first = int((n - 1) * n / 2) + 1
    last = first + n
    return np.prod(range(first, last)) + compute_prod_seq_term(n-1)

def compute_prod_better(n):
    '''

    '''

    def recurse(c, i):
        if c == n + 1:
            return 0 
        else:
            v = np.prod(range(i, i + c))
            return v + recurse(c + 1, i + c)
    return recurse(1, 1)

if __name__ == '__main__':
    inputs = [
    1,
    5,
    7
    ]
    expect = [
    1,
    365527,
    6006997207
    ]
    for i,e in zip(inputs, expect):
        print(e)
        print(compute_prod_seq_term(i))
        print(compute_prod_better(i))