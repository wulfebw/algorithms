"""
:keywords: probability, biased, random
"""

import random

def biased_random(p=.1):
    """
    :description: returns 0 with p probability and 1 o/w
    """
    if random.random() < p:
        return 0
    return 1

def unbiased_random():
    """
    :description: uses a biased random sampling with unknown bias to achieve an unbiased sampling

    :time:
    :space: 
    """
    pass





if __name__ == '__main__':
    runs = 1000
    total = 0
    for i in runs:
        total += unbiased_random()
    avg = total / runs
    print 'average value after {} runs: {}'.format(runs, avg)