'''
recursive backtracking is sort of an extension of exhaustive search wherein 
it does not expand parts of a the search tree when it knows that they are not 
useful. 

key point: backtracking search searches for paths through the tree 
contrast this with breadth and depth first search
these search methods are looking for specific vertices in a graph 
- where, since we don't revise we kind of treat that graph as a tree
'''


from context_timer import ContextTimer
import numpy as np
import sys
sys.path.append('../trees')

import trie

def shrink_word(w, lexicon):
    if len(w) == 0:
        return True, []
    elif not lexicon.contains(w):
        return False, [w]
    else:
        for i, l in enumerate(w):
            res, lst = shrink_word(w[:i] + w[i+1:], lexicon)
            if res:
                return True, [w] + lst
        return False, lst

def run_shrink_word():
    t = trie.Trie()
    t.load_english(maxlen=6)
    words = [
        'smart',
        'father',
        'lymph',
        'rope'
    ]
    for word in words:
        res, lst = shrink_word(word, t)
        print(res)
        print(lst)
        print()

def cubic_decomp(n):
    '''
    complexity?
    the recursion is like T(n) = T(n-1) + T(n-2) + T(n-3) + ...
    = sum i = n-1 to 1 T(i)
    so definitely exponential 
    but it just so happens that most numbers are decomposed easily I guess
    '''

    def recurse(r, n, max_terms):
        if r == 0: return True, []
        if max_terms <= 0: return False, []
        if r < 0: return False, []
        for i in range(n - 1, 0, -1):
            res, terms = recurse(r - i ** 3, i, max_terms - 1)
            if res:
                return True, terms + [i]
        return False, []

    return recurse(n ** 3, n, 10)

def cubic_decomp_dp(n):
    '''
    fills a n^3 x n grid so O(n^4) time + O(n^4) space
    so just doesn't work at all for large instances
    - note though that this is better than the worst case recursive solution 
        above because it seems like that solution is exponential
    - of course that solution returns typically before then, so it ends up 
        being faster
    '''
    m = n ** 3
    v = np.zeros((m+1,n+1), dtype=bool)
    v[0,:] = True
    for i in range(m):
        for j in range(n):
            v[i+1,j+1] = v[i+1,j] or v[i+1 - j ** 3, j]
    return v[-1,-1]

def run_cubic_decomp():
    for n in [5, 6, 11, 35, 1021, 11111]:
        print(n)
        with ContextTimer():
            print(cubic_decomp(n)[0])
        with ContextTimer():
            print(cubic_decomp_dp(n))
        print()

def eight_queens(n):
    '''
    characteristics of this problem I hadn't previously seen 
    1. calling recurse with n+1 (i.e., going from the bottom to the top)
        and having the top be the one that knows?
        err, no that's not it, what's different about this?
    '''
    board = np.zeros((n,n))

    def is_valid_board(a, row, col):
        # check rows to the left 
        for i in range(col):
            if a[row, i] == 1:
                return False

        # check upper left diagonal
        for (i,j) in zip(range(row,-1,-1), range(col,-1,-1)):
            if a[i,j] == 1:
                return False

        # check lower left diagonal
        for (i,j) in zip(range(row,a.shape[0]), range(col,-1,-1)):
            if a[i,j] == 1:
                return False

        return True

    def recurse(ncol):
        if ncol == n:
            return True
        else:
            for i in range(n):
                if is_valid_board(board, i, ncol):
                    board[i, ncol] = 1
                    if recurse(ncol + 1):
                        return True 
                    board[i, ncol] = 0
            return False

    recurse(0)
    return board

def run_eight_queens():
    for n in [5, 8]:
        board = eight_queens(n)
        print(board)
        print()

if __name__ == '__main__':
    run_shrink_word()
    run_cubic_decomp()
    run_eight_queens()




















