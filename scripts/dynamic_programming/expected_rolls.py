'''
game involves a 1d board with numbers 
you start on the left and end when you get past the last square 
each time you roll a die 
whatever it lands on 
multiply that by the cotents of your current square
and move forward in the array by that amount 

question:
what is the expected number of steps it will take to reach the end?
'''

import numpy as np

def simulate_expected_rolls(a, runs=100000):
    '''
    runs simulations to get approximate value with which to compare
    '''
    n = len(a)
    total = 0
    for r in range(runs):
        i = 0
        count = 0
        while i < n:
            count += 1
            i += np.random.randint(1,6+1) * a[i]
        total += count 
    return total / runs


def expected_rolls(a):
    '''
    DP approach wherein you compute the expected value and probability for 
    each square, and build up as you go 
    O(n)
    '''
    n = len(a)
    e = np.zeros(n+1)
    p = np.zeros(n+1)
    p[0] = 1

    for i in range(n):

        for j in range(1, 6+1):
            nxt = i + a[i] * j
            nxt = -1 if nxt >= n else nxt
            
            e[nxt] = (e[nxt] * p[nxt] + (e[i] + 1) * p[i] * 1/6) / (p[nxt] + p[i] * 1/6 + 1e-16)
            p[nxt] = p[nxt] + p[i] * 1/6 + 1e-16

    return e[-1]

if __name__ == '__main__':
    np.random.seed(1)
    inputs = [
        [1],
        [1,1],
        [1,1,1],
        [1,2,3,4,5],
        np.random.randint(1,6,5000)
    ]

    for i in inputs:
        print('actual:\t{:.5f}'.format(expected_rolls(i)))
        # print('sim:\t{:.5f}'.format(simulate_expected_rolls(i)))



