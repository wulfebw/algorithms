
import collections
import numpy as np

import context_timer as ct

def count_substr_occurrences(s, sub):
    n, m = len(s), len(sub)
    count = 0
    for i in range(n - m + 1):
        if s[i:i+m] == sub:
            count += 1
    return count

def maximize_string_function_naive(s):
    '''
    analysis:
    - 2 for loops 
        + each calls count_substr_occurrences
            * which is O(n^2) (not positive that's tight)
    - therefore O(n^4)

    '''
    n = len(s)
    maxscore = 0
    for i in range(n):
        for j in range(i+1, n+1):
            score = (j - i) * count_substr_occurrences(s, s[i:j])
            maxscore = max(maxscore, score)
    return maxscore

def maximize_string_function_naive_space(s):
    '''
    analysis:
    - O(n^2)
    '''
    n = len(s)
    counts = collections.defaultdict(int)
    for i in range(n):
        for j in range(i+1, n+1):
            counts[s[i:j]] += 1

    best = 0
    for (k,v) in counts.items():
        best = max(best, len(k) * v)
    return best



if __name__ == '__main__':

    n_tests = 10
    length = 100
    tests = np.random.randint(ord('A'), ord('B') + 1, size=n_tests * length)
    tests = tests.reshape(n_tests, length)
    letter_tests = [''.join([chr(v) for v in tests[i]]) for i in range(n_tests)]

    for s in letter_tests:
        print(s)
        expected = maximize_string_function_naive(s)
        actual = maximize_string_function_naive_space(s)
        print(expected)
        print(actual)
