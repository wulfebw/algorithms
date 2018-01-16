'''
I think the difference between finding the lcsubstring and lcsubseq is that in the substring case you erase your progress, whereas with the subsequence you do not
'''

import numpy as np

def lcs(a,b):
    n, m = len(a), len(b)
    v = np.zeros((n+1, m+1))
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                v[i+1,j+1] = v[i,j] + 1
    return int(v.max())


if __name__ == '__main__':
    inputs = [
        ('GeeksforGeeks', 'GeeksQuiz'),
        ('abcdxyz', 'xyzabcd'),
        ('zxabcdezy', 'yzabcdezx'),
        ('aabbbccccddd', 'dddddbbbbbbaaaaacccc')
    ]
    expect = [
        5,
        4,
        6,
        4
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(lcs(*i))
        print()
