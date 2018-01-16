
import numpy as np

def edit_dist(s1,s2):
    '''
    The idea here is the same roughly as the longest common subsequence
    basically moving backward through one of the strings, for each letter
    iterating over the other string 

    you decide whether to "insert" a value into this string. inserting would 
    mean you don't change the current letter for the first string, but do 
    change letters for the other string - is that insert after or before the 
    current letter?

    or you could "remove" from this string, in which case you don't change 
    letters for the other string but do change for the first string

    "replace" - in this case, you move back 1 letter in both strings
    '''
    n, m = len(s1), len(s2)
    v = np.zeros((n+1,m+1))
    v[:,0] = np.arange(n+1)
    v[0,:] = np.arange(m+1)
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                v[i+1,j+1] = v[i,j] 
            else:
                mincost = 1 + min(v[i,j], v[i+1,j], v[i,j+1])
                v[i+1,j+1] = mincost

    return int(v[-1,-1])

if __name__ == '__main__':
    inputs = [
        ('geek','gesek'),
        ('cat', 'cut'),
        ('saturday', 'sunday'),
        ('abababab', 'bbbb')
    ]
    expect = [
        1,
        1,
        3,
        4
    ]

    for (i,e) in zip(inputs, expect):
        print(e)
        print(edit_dist(*(i)))
        print()