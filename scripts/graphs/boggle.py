
import numpy as np
import sys

sys.path.append('../trees')

import trie

def boggle(b, lex, minlen):

    visit = np.zeros(b.shape, dtype=bool)

    def boggle_neighbors(b, i, j, visit):
        nrows, ncols = b.shape
        for v in [-1,0,1]:
            for h in [-1,0,1]:
                if v == 0 and h == 0:
                    continue
                ni = i + v 
                nj = j + h 
                if ni >= 0 and ni < nrows and nj >= 0 and nj < ncols and not visit[ni,nj]:
                    yield(ni,nj)

    def recurse(i, j, prefix):
        prefix += b[i,j]
        if lex.contains(prefix) and len(prefix) > minlen:
            yield prefix
        if lex.is_prefix(prefix):
            for (ni,nj) in boggle_neighbors(b, i, j, visit):
                visit[ni,nj] = True
                yield from recurse(ni, nj, prefix)
                visit[ni,nj] = False

    n, m = b.shape
    for i in range(n):
        for j in range(m):
            visit[i,j] = True
            yield from recurse(i, j, '')
            visit[i,j] = False

def random_board(n):
    b = np.empty((n,n), dtype=str)
    for i in range(n):
        for j in range(n):
            b[i,j] = chr(np.random.randint(low=ord('a'), high=ord('z')+1))
    return b

if __name__ == '__main__':
    lex = trie.Trie()
    words = ['abc','bcd','abcd','bb']
    for word in words:
        lex.insert(word)
    b = np.array([
        ['a','b'],
        ['c','d'],
    ])
    for word in boggle(b, lex, minlen=1):
        print(word)

    # random 
    b = random_board(8)
    print(b)
    lex = trie.Trie()
    lex.load_english(maxlen=8)
    for word in sorted(boggle(b, lex, minlen=4)):
        print(word)
