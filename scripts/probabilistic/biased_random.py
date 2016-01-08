"""
:keywords: probability, biased, random
"""

import random

def biased_random(p=.1):
    """
    :description: returns 1 with p probability and 0 o/w
    """
    if random.random() < p:
        return 1
    return 0

def unbiased_random():
    """
    :description: uses a biased random sampling with unknown bias to achieve an unbiased sampling

    :time: O(1/(p * (1-p))) - the probability that the while loop stops is the same as the probability that one variable is 0 and the other 1. This is equal to p * (1-p). So the expected run time is the number of coin flips with heads probability p * (1-p) until you get a heads. This is the binomial distribution with expected value 1/probability heads, which in this case is 1/(.1 * .9) = 1/.09 = 11.1. 
        Which is actually wrong, it should be either p(1-p) or (1-p)p, doubling the probability of leaving the loop, therefore this should be O(2/(p * (1-p))), which actually should be O(1/p)
    :space: O(1)
    """
    x = y = 0
    counter = 0
    while x == y:
        counter += 1
        x = biased_random()
        y = biased_random()
    return x, counter

if __name__ == '__main__':
    runs = 10000
    total = 0
    total_counter = 0
    for i in range(runs):
        cur_total, cur_counter = unbiased_random()
        total += cur_total
        total_counter += cur_counter
    avg = total / float(runs)
    avg_counter = total_counter / float(runs)
    print 'average value and counter after {} runs: {}\t counter: {}'.format(runs, avg, avg_counter)

"""
:additional notes: to get an unbiased estimator from a biased estimator, or generally to undue some sampling bias, find two secondary random variables that combine earlier ones and then decide between them equally
"""