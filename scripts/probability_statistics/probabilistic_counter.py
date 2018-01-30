"""
:keywords: probability
"""

import random

def squared(counter):
    cur = 2 ** (counter - 1)
    prev = 2 ** (counter - 2)
    return 1.0 / (cur - prev)

def identity(counter):
    cur = counter
    prev = counter - 1
    return 1 / (cur - prev)

def increment(counter, probability_function):
    """
    :description: probabilistically increments a counter variable, where the counter value determines the probability of being incremented. This effectively enables a set of bits to hold the values of a counter for much higher increment counts provided that the counter can be less precise.

    :time: O(1)
    :space: O(1)
    """
    increment_probability = probability_function(counter)
    if random.random() < increment_probability:
        counter += 1
    return counter

def run(probability_function):
    counter = 1
    for i in range(1000):
        counter = increment(counter, probability_function)
    print counter

if __name__ == '__main__':
    run(squared)

"""
:additional notes:
"""